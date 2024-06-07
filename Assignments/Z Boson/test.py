# -*- coding: utf-8 -*-
"""
Z^0 Boson

Author: r40563tb
"""
import numpy as np
from scipy.optimize import curve_fit
from scipy.optimize import OptimizeWarning
import os
import matplotlib.pyplot as plt

CONVERSION_FACTOR = 0.3894e6
GAMMA_EE = 83.91e-3
INITIAL_GUESS = [90, 3]


def read_input_data(*csvfiles):
    """
    Read data from CSV files and return a tuple containing numpy arrays.

    Parameters
    ----------
    *csvfiles : str
        Variable number of CSV file paths.

    Returns
    -------
    tuple
        Tuple of numpy arrays containing the loaded data from CSV files.

    Raises
    ------
    FileNotFoundError
        If any of the specified CSV files do not exist.
    ValueError
        If CSV files have different numbers of columns, if the files cannot be loaded,
        or if there is an issue with loading data from any of the files.

    Notes
    -----
    The function uses `numpy.genfromtxt` to load data from CSV files. It skips header rows,
    handles missing values, and fills in specified values for missing data.

    If an issue occurs during data loading, such as a mismatch in the number of columns
    or the inability to load data from a specific file, the function raises a ValueError
    indicating the problematic file.
    """
    successful_data = []

    for csvfile in csvfiles:
        if not os.path.exists(csvfile):
            raise FileNotFoundError(f"File not found: {csvfile}")

    problematic_file = None

    for csvfile in csvfiles:
        try:
            data = np.genfromtxt(
                csvfile,
                comments='%',
                delimiter=',',
                skip_header=1,
                dtype=float,
                missing_values='fail',
                filling_values=np.nan
            )
            successful_data.append(data)
        except ValueError as ve:
            problematic_file = csvfile
            break

    if problematic_file:
        raise ValueError(
            f"{problematic_file}: CSV files have different numbers of columns or cannot be loaded.")

    num_columns_set = set(data.shape[1] for data in successful_data)
    if len(num_columns_set) > 1:
        raise ValueError("CSV files have different numbers of columns.")

    return tuple(successful_data)


def clean_data(*datasets, remove_outliers=True, z_score_threshold=3):
    """
    Clean data by removing rows with NaN or negative values, and optionally remove outliers.

    Parameters
    ----------
    *datasets : numpy arrays
        Variable number of datasets.
    remove_outliers : bool, optional
        If True, remove outliers based on z-scores. Defaults to True.
    z_score_threshold : float, optional
        Z-score threshold for outlier removal. Defaults to 3.

    Returns
    -------
    tuple
        Tuple of cleaned numpy arrays.
    """
    cleaned_data = []

    for dataset in datasets:
        # Remove rows with NaN or negative values
        filtered_data = dataset[~np.isnan(dataset).any(
            axis=1) & (np.all(dataset > 0, axis=1))]

        if remove_outliers:
            z_scores = np.abs(
                (filtered_data - np.mean(filtered_data, axis=0)) / np.std(filtered_data, axis=0))
            # Keep only the rows within the z-score threshold for each column
            filtered_data = filtered_data[(
                z_scores <= z_score_threshold).all(axis=1)]

        cleaned_data.append(filtered_data.astype(float))

    return tuple(cleaned_data)


def model_function(energy, m_z, gamma_z, gamma_ee=GAMMA_EE):
    """
    Calculate the model prediction.

    Parameters
    ----------
    energy : numpy array
        Input values (center-of-mass energy).
    m_z : float
        Resonance mass parameter.
    gamma_z : float
        Resonance width parameter.
    gamma_ee : float, optional
        Electron coupling parameter (default is GAMMA_EE).

    Returns
    -------
    numpy array
        Model predictions.
    """
    sigma = CONVERSION_FACTOR * (12 * np.pi / m_z**2) * (energy**2 /
                                                         ((energy**2 - m_z**2)**2 + m_z**2 * gamma_z**2)) * gamma_ee**2
    return sigma


def fit_to_model_function(energy, cross_section, uncertainty,
                          initial_guess=INITIAL_GUESS, residual_threshold=8.0,
                          z_score_threshold=5.0, max_iterations=1000):
    """
    Fit observed cross-section data to a model expression using curve_fit from
    scipy.optimize.

    Parameters
    ----------
    energy : numpy array
        Input values (center-of-mass energy).
    cross_section : numpy array
        Observed cross-section values.
    uncertainty : numpy array
        Uncertainty on the cross-section values.
    initial_guess : list
        Initial guess for the parameters.
    threshold : float, optional
        Threshold for identifying and removing outliers during each iteration.
    max_iterations : int, optional
        Maximum number of iterations for the outlier removal and re-fitting
        process.

    Returns
    -------
    tuple
        Tuple containing optimal parameters and covariance matrix obtained
        after fitting.

    """
    for iteration in range(max_iterations):
        try:
            optimal_params, covariance = curve_fit(
                model_function, energy, cross_section, p0=initial_guess,
                sigma=uncertainty, check_finite=True, maxfev=10000)

            fitted_values = model_function(energy, *optimal_params)
            residuals = cross_section - fitted_values
            z_scores = (residuals - np.mean(residuals)) / np.std(residuals)
            outlier_indices = np.where(
                (np.abs(residuals) > residual_threshold) | (np.abs(z_scores) > z_score_threshold))[0]

            print(f"Iteration {iteration + 1}:")
            print("Outlier Indices:", outlier_indices)
            print("Removed Energies:", energy[outlier_indices])
            print("Shape of energy:", energy.shape)
            print("Removed Cross Sections:", cross_section[outlier_indices])
            print("Shape of cross-section:", cross_section.shape)
            print("Optimal Parameters:", optimal_params)

            if len(outlier_indices) == 0:
                break

            initial_guess = optimal_params

            energy, cross_section, uncertainty, residuals = remove_outliers(
                energy, cross_section, uncertainty, residuals, outlier_indices)

        except (OptimizeWarning, RuntimeError) as e:
            print(f"Fit failed in iteration {iteration + 1}. Reason: {e}")

    plot_residuals(energy, residuals)

    return optimal_params, covariance, energy, cross_section, uncertainty, iteration


def remove_outliers(energy, cross_section, uncertainty, residuals, outlier_indices):
    """
    Remove outliers from the data and residuals based on provided indices.

    Parameters
    ----------
    energy : numpy array
        Input values (center-of-mass energy).
    cross_section : numpy array
        Observed cross-section values.
    uncertainty : numpy array
        Uncertainty on the cross-section values.
    residuals : numpy array
        Residuals of the fit.
    outlier_indices : numpy array
        Indices of the outliers to be removed.

    Returns
    -------
    tuple
        Tuple of numpy arrays containing the cleaned data and residuals.
    """
    cleaned_energy = np.delete(energy, outlier_indices)
    cleaned_cross_section = np.delete(cross_section, outlier_indices)
    cleaned_uncertainty = np.delete(uncertainty, outlier_indices)
    cleaned_residuals = np.delete(residuals, outlier_indices)

    return cleaned_energy, cleaned_cross_section, cleaned_uncertainty, cleaned_residuals


def plot_residuals(cleaned_energy, cleaned_residuals):
    """
    Plot two residual plots using subplots.

    Parameters
    ----------
    original_energy : numpy array
        Original input values (center-of-mass energy) before outlier removal.
    original_residuals : numpy array
        Residuals of the fit using the original data.
    cleaned_energy : numpy array
        Input values (center-of-mass energy) after outlier removal.
    cleaned_residuals : numpy array
        Residuals of the fit using the outlier-removed data.
    """
    # Plot residuals using subplots
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))

    axs[0].plot(cleaned_energy, cleaned_residuals, 'o')
    axs[0].axhline(y=0, color='r', linestyle='--')
    axs[0].set_title('Residual Plot (Outlier-Removed Data)')
    axs[0].set_xlabel('Energy (GeV)')
    axs[0].set_ylabel('Residuals (nb)')

    # Plot histogram of residuals
    axs[1].hist(cleaned_residuals, bins=30, edgecolor='black', alpha=0.7)
    axs[1].set_title('Histogram of Residuals (Outlier-Removed Data)')
    axs[1].set_xlabel('Residuals (nb)')
    axs[1].set_ylabel('Frequency')

    plt.tight_layout()
    plt.savefig('cleaned_residuals.png', dpi=600)
    plt.show()


def display_optimal_parameters(parameters):
    """
    Display the optimal parameters.

    Parameters
    ----------
    parameters : list
        Optimal parameters.
    """
    print("Optimal Parameters:")
    print(f"Parameter 1: {parameters[0]}")
    print(f"Parameter 2: {parameters[1]}")


def calculate_reduced_chi_squared(observed, expected, uncertainties, num_parameters):

    def calculate_chi_squared():
        residuals = observed - expected
        chi_squared = np.sum((residuals / uncertainties)**2)
        return chi_squared

    chi_squared = calculate_chi_squared()
    dof = len(observed) - num_parameters
    reduced_chi_squared = chi_squared / dof
    return reduced_chi_squared


def plot_data_and_fit(x, y, uncertainties, optimal_parameters):
    """
    Plot the original data and the fitted curve with error bars.

    Parameters
    ----------
    x : numpy array
        Input values.
    y : numpy array
        Actual data values.
    optimal_parameters : list
        Optimal parameters for the fitted curve.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.errorbar(x, y, yerr=uncertainties, fmt='o',
                label='Cleaned Data', color='blue')

    x_range = np.linspace(min(x), max(x), 1000)
    model_predictions = model_function(x_range,
                                       optimal_parameters[0], optimal_parameters[1])
    ax.plot(x_range, model_predictions, label='Fitted Curve', color='red')
    ax.legend()
    ax.set_xlabel('Centre-of-mass energy (GeV)')
    ax.set_ylabel('Cross section (nb)')
    plt.savefig('fitted_curve_plot.png', dpi=600)
    plt.show()


def main():
    """
    Main function to demonstrate reading, cleaning, and combining data from CSV files.

    Notes
    -----
    Example usage:
    - Specify CSV file paths in the 'csvfiles' list.
    - The 'read_input_data' function is called to load data from CSV files.
    - The 'clean_data' function is called to remove rows with NaN or negative values.
    - The cleaned datasets are combined using 'numpy.vstack'.
    - The 'plot_combined_data' function is called to visualize the combined data.
    """
    csvfiles = ['z_boson_data_1.csv', 'z_boson_data_2.csv']

    try:
        loaded_data = read_input_data(*csvfiles)
        cleaned_data = clean_data(
            *loaded_data, remove_outliers=False, z_score_threshold=3)
        combined_data = np.vstack(cleaned_data)
        energy, cross_section, uncertainties = combined_data.T
        optimal_parameters, covariance, energy, cross_section, uncertainty, iteration = fit_to_model_function(
            energy, cross_section, uncertainties)

        display_optimal_parameters(optimal_parameters)

        print("Shape of energy:", energy.shape)
        print("Shape of cross-section:", cross_section.shape)

        plot_data_and_fit(energy, cross_section,
                          uncertainty, optimal_parameters)

        reduced_chi_squared = calculate_reduced_chi_squared(cross_section, model_function(
            energy, *optimal_parameters), uncertainty, len(optimal_parameters))
        print(reduced_chi_squared)
        print(covariance)
        print(f"This was completed in {iteration} iterations.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
