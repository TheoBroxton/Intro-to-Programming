# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:51:52 2023

@author: theob
"""
# -*- coding: utf-8 -*-
"""
Z^0 Boson

Author: r40563tb
"""

import numpy as np
from scipy.optimize import curve_fit
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
        If CSV files have different numbers of columns or if the files cannot be loaded.

    Notes
    -----
    The function uses `numpy.genfromtxt` to load data from CSV files. It skips header rows,
    handles missing values, and fills in specified values for missing data.
    """
    for csvfile in csvfiles:
        if not os.path.exists(csvfile):
            raise FileNotFoundError(f"File not found: {csvfile}")

    loaded_data = tuple(
        np.genfromtxt(
            csvfile,
            comments='%',
            delimiter=',',
            skip_header=1,
            dtype=float,
            missing_values='fail',
            filling_values=np.nan
        )
        for csvfile in csvfiles
    )

    # Check if all datasets have the same number of columns
    num_columns_set = set(data.shape[1] for data in loaded_data)
    if len(num_columns_set) > 1:
        raise ValueError("CSV files have different numbers of columns.")

    return loaded_data


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


def fit_and_evaluate(energy, cross_section, uncertainty, initial_guess, residual_threshold, z_score_threshold):
    # Initial fit to obtain optimal parameters
    optimal_params, covariance = curve_fit(
        model_function, energy, cross_section, p0=initial_guess, sigma=uncertainty, check_finite=True, maxfev=10000)

    # Calculate residuals and z-scores based on initial fit
    residuals = cross_section - model_function(energy, *optimal_params)
    z_scores = residuals / uncertainty

    # Identify outliers based on thresholds
    outlier_indices = np.where((np.abs(residuals) > residual_threshold) | (
        np.abs(z_scores) > z_score_threshold))[0]

    # Exclude outliers from the dataset
    energy_clean = np.delete(energy, outlier_indices)
    cross_section_clean = np.delete(cross_section, outlier_indices)
    uncertainty_clean = np.delete(uncertainty, outlier_indices)

    # Refit the model with the cleaned dataset
    optimal_params_clean, covariance_clean = curve_fit(
        model_function, energy_clean, cross_section_clean, p0=initial_guess, sigma=uncertainty_clean, check_finite=True, maxfev=10000)

    # Calculate reduced chi-squared with the cleaned dataset
    residuals_clean = cross_section_clean - \
        model_function(energy_clean, *optimal_params_clean)
    dof_clean = len(energy_clean) - len(optimal_params_clean)
    chi_squared_red_clean = np.sum(
        (residuals_clean / uncertainty_clean)**2) / dof_clean

    return optimal_params_clean, covariance_clean, energy_clean, cross_section_clean, chi_squared_red_clean


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
    plt.savefig('grid_searched.png', dpi=600)
    plt.show()


def plot_combined_data(combined_data, save_path='scatter_plot.png'):
    """
    Plot the combined data with uncertainties and save the figure as a PNG file.

    Parameters
    ----------
    combined_data : numpy array
        Combined data to be plotted.
    save_path : str, optional
        File path to save the figure as a PNG file. Defaults to 'scatter_plot.png'.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    x_values = combined_data[:, 0]
    y_values = combined_data[:, 1]
    uncertainties = combined_data[:, 2]

    ax.errorbar(x_values, y_values, yerr=uncertainties,
                fmt='o', label='Data with Uncertainties')
    ax.set_title('Scatter Plot with Uncertainties')
    ax.set_xlabel('Centre-of-mass energy (GeV)')
    ax.set_ylabel('Cross section (nb)')
    ax.legend()

    plt.savefig(save_path, bbox_inches='tight', dpi=600)
    plt.show()
    plt.close()


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
        # plot_combined_data(combined_data)
        x, y, uncertainties = combined_data.T
        residual_thresholds = np.linspace(0.1, 10, 20)
        z_score_thresholds = np.linspace(0.1, 10, 20)

        best_residual_threshold = None
        best_z_score_threshold = None
        best_chi_squared_red = np.inf

        initial_guess = INITIAL_GUESS
        for residual_threshold in residual_thresholds:
            for z_score_threshold in z_score_thresholds:
                _, _, _, _, chi_squared_red = fit_and_evaluate(
                    x, y, uncertainties, initial_guess, residual_threshold, z_score_threshold)

                if chi_squared_red < best_chi_squared_red:
                    best_chi_squared_red = chi_squared_red
                    best_residual_threshold = residual_threshold
                    best_z_score_threshold = z_score_threshold

        print("Best Residual Threshold:", best_residual_threshold)
        print("Best Z-score Threshold:", best_z_score_threshold)
        print("Best Reduced Chi-squared:", best_chi_squared_red)

        # Now you can use the best thresholds for the final fit
        optimal_params_final, covariance_final, energy_final, cross_section_final, _ = fit_and_evaluate(
            x, y, uncertainties, initial_guess, best_residual_threshold, best_z_score_threshold)

        # Plot the final fit with the cleaned dataset
        # plt.plot(x, y, 'o', label='Observed Data (Original)')
        plt.plot(energy_final, model_function(energy_final, *
                 optimal_params_final), label='Final Fit (Cleaned)')
        plt.xlabel('Energy (units)')
        plt.ylabel('Cross Section (units)')
        plt.legend()
        plt.show()

        # display_optimal_parameters(optimal_parameters)
        # plot_data_and_fit(x, y, uncertainties, optimal_parameters)

        # reduced_chi_squared = calculate_reduced_chi_squared(y, model_function(
        #     x, *optimal_parameters), uncertainties, len(optimal_parameters))
        # print(reduced_chi_squared)
        # print(covariance)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
