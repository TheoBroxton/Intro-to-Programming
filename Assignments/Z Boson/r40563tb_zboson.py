# -*- coding: utf-8 -*-
"""
--------------TITLE--------------.

PHYS20161 - Assignment 2 - Z^0 Boson
---------------------------------
This Python script performs data analysis on Z boson resonance experiments.

It does this by:
    1) Reading in data from specified CSV files in the 'csvfiles' list with the
       function 'read_input_data'.
    2) Cleaning data of rows containting negative or NaN values using
       'clean_data'
    3) Fitting the combined, clean data to a model function defined in
       'model_function' with curve_fit from SciPy in 'fit_to_model_function'.
       The exact specifications of the fit and outlier removal can be altered
       by the user.
    4) Visualising the data in informative plots which are displayed and saved.
    5) Returning values of interest to the user after the analysis.

Last updated: 20/12/23
Author: r40563tb
"""
import numpy as np
import scipy.constants as pc
from scipy.constants import electron_volt
from scipy.optimize import curve_fit, OptimizeWarning
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
        If CSV files have different numbers of columns, if the files cannot be
        loaded, or if there is an issue with loading data from any of the
        files.

    Notes
    -----
    The function uses `numpy.genfromtxt` to load data from CSV files. It skips
    header rows and handles missing values. The exact way it loads the file can
    be altered with the arguments of genfromtxt.

    If an issue occurs during data loading, such as a mismatch in the number of
    columns or the inability to load data from a specific file, the function
    raises a ValueError indicating the problematic file.
    """
    successful_data = []

    for csvfile in csvfiles:
        if not os.path.exists(csvfile):
            raise FileNotFoundError(f"File not found: {csvfile}")

    problematic_file = None

    for csvfile in csvfiles:
        try:
            data = np.genfromtxt(csvfile, comments='%', delimiter=',',
                                 skip_header=1, dtype=float,
                                 missing_values='fail', filling_values=np.nan)
            successful_data.append(data)
        except ValueError:
            problematic_file = csvfile
            break

    if problematic_file:
        raise ValueError(
            f"{problematic_file}: CSV files have different numbers of columns "
            "or cannot be loaded.")

    num_columns_set = set(data.shape[1] for data in successful_data)
    if len(num_columns_set) > 1:
        raise ValueError("CSV files have different numbers of columns.")

    return tuple(successful_data)


def clean_data(*datasets, remove_outliers=True, z_score_threshold=3):
    """
    Clean data by removing rows with NaN or negative values (and outliers).

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
        filtered_data = dataset[~np.isnan(dataset).any(
            axis=1) & (np.all(dataset > 0, axis=1))]

        if remove_outliers:
            z_scores = np.abs(
                (filtered_data - np.mean(filtered_data, axis=0)) /
                np.std(filtered_data, axis=0))

            filtered_data = filtered_data[(
                z_scores <= z_score_threshold).all(axis=1)]

        cleaned_data.append(filtered_data.astype(float))

    return tuple(cleaned_data)


def model_function(energy, m_z, gamma_z, partial_width=GAMMA_EE):
    """
    Calculate the model prediction.

    The default model is for a Breit-Wigner distribution, with cross-section as
    the vertical and energy as the horizontal axes. The conversion factor is
    there to convert the equation from natural units.

    Parameters
    ----------
    energy : numpy array
        Input values (center-of-mass energy).
    m_z : float
        Resonance mass parameter.
    gamma_z : float
        Resonance width parameter.
    partial_width : float, optional
        Partial width for the final state of interest (default is GAMMA_EE for
        a Z^0 -> e^-e^+ decay).

    Returns
    -------
    sigma : numpy array
        Model predictions.
    """
    sigma = (CONVERSION_FACTOR * (12 * np.pi / m_z**2) *
             (energy**2 / ((energy**2 - m_z**2)**2 + m_z**2 * gamma_z**2)) *
             partial_width**2)
    return sigma


def fit_to_model_function(energy, cross_section, uncertainty,
                          initial_guess=INITIAL_GUESS, residual_threshold=8.0,
                          z_score_threshold=5.0,
                          method='lm', max_iterations=1000):
    """
    Fit observed cross-section data to a model expression.

    This function utilizes the curve_fit function from scipy.optimize to
    optimize parameters and estimate covariance of the fitted parameters for a
    given model expression and observed data. The parameters of the fit can be
    taylored by the user for their desired results.

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
    residual_threshold : float, optional
        Threshold for identifying and removing outliers based on residuals
        during each iteration.
    z_score_threshold : float, optional
        Threshold for identifying and removing outliers based on their z-scores
        during each iteration.
    method : str, optional
        Optimization method ('lm', 'trf', 'dogbox', etc.). If none is
        specified, the default method will be the Levenberg-Marquardt
        algorithm.
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
                sigma=uncertainty, check_finite=True, method=method,
                maxfev=10000)

            fitted_values = model_function(energy, *optimal_params)
            residuals = cross_section - fitted_values
            z_scores = (residuals - np.mean(residuals)) / np.std(residuals)
            outlier_indices = np.where(
                (np.abs(residuals) > residual_threshold) |
                (np.abs(z_scores) > z_score_threshold))[0]

            if len(outlier_indices) == 0:
                break

            initial_guess = optimal_params

            energy, cross_section, uncertainty, residuals = remove_outliers(
                energy, cross_section, uncertainty, residuals, outlier_indices)

        except (OptimizeWarning, RuntimeError) as e:
            print(f"Fit failed in iteration {iteration + 1}. Reason: {e}")

    plot_residuals(energy, residuals)

    lifetime = pc.hbar / (1e9 * electron_volt * optimal_params[1])
    lifetime_uncertainty = lifetime * (uncertainty[1] / optimal_params[1])

    return (optimal_params, covariance, energy, cross_section, uncertainty,
            iteration, lifetime, lifetime_uncertainty)


def remove_outliers(energy, cross_section, uncertainty, residuals,
                    outlier_indices):
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

    return (cleaned_energy, cleaned_cross_section, cleaned_uncertainty,
            cleaned_residuals)


def plot_residuals(cleaned_energy, cleaned_residuals):
    """
    Plot two residual plots as subplots.

    It contains a scatter plot against the model fit to see which energies
    contain residuals of larger magnitude. Below which is a histogram showing
    the frequency of the magnitude of the residuals. Together they should help
    the user to have a better understanding of the residuals on the performed
    fit.

    Parameters
    ----------
    cleaned_energy : numpy array
        Input values (center-of-mass energy) after outlier removal.
    cleaned_residuals : numpy array
        Residuals of the fit using the outlier-removed data.
    """
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))

    axs[0].plot(cleaned_energy, cleaned_residuals, 'o')
    axs[0].axhline(y=0, color='r', linestyle='--')
    axs[0].set_title('Residual Plot')
    axs[0].set_xlabel('Energy (GeV)')
    axs[0].set_ylabel('Residuals (nb)')

    axs[1].hist(cleaned_residuals, bins=30, edgecolor='black', alpha=0.7)
    axs[1].set_title('Histogram of Residuals')
    axs[1].set_xlabel('Residuals (nb)')
    axs[1].set_ylabel('Frequency')

    plt.tight_layout()
    plt.savefig('cleaned_residuals.png', dpi=600)
    plt.show()
    plt.close()


def calculate_reduced_chi_squared(observed, expected, uncertainties,
                                  num_parameters):
    """
    Calculate the reduced chi-squared statistic for goodness-of-fit assessment.

    Parameters
    ----------
    observed : numpy array
        The observed data.
    expected : numpy array
        The expected values from a model function.
    uncertainties : numpy arry
        The uncertainties associated with the observed data.
    num_parameters : int
        The number of parameters in the model.

    Returns
    -------
    reduced_chi_squared : float
        The calculated reduced chi-squared statistic.

    """

    def calculate_chi_squared():
        """
        Calculate the chi-squared statistic for the given data and model.

        Returns
        -------
        chi_squared : float
            The calculated chi-squared statistic.

        """
        residuals = observed - expected
        chi_squared = np.sum((residuals / uncertainties)**2)
        return chi_squared

    chi_squared = calculate_chi_squared()
    dof = len(observed) - num_parameters
    reduced_chi_squared = chi_squared / dof
    return reduced_chi_squared


def plot_data_and_fit(x, y, uncertainties, optimal_parameters):
    """
    Plot the cleaned data and the fitted curve with error bars.

    Parameters
    ----------
    x : numpy array
        Input values.
    y : numpy array
        Actual data values.
    optimal_parameters : list
        Optimal parameters for the fitted curve.
    """
    def find_crossings(x_values, y_values, threshold):
        """
        Find the indices where a curve crosses a specified threshold value.

        Parameters
        ----------
        x_values : numpy array
            The x-values corresponding to the curve.
        y_values : numpy array
            The y-values of the curve.
        threshold : float
            The threshold value for determining the crossings.

        Returns
        -------
        crossings : numpy array
            An array containing the indices where the curve crosses the
            threshold.
        """
        above_threshold = y_values > threshold
        crossings = np.where(np.diff(above_threshold))[0]
        return crossings

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.errorbar(x, y, yerr=uncertainties, fmt='o',
                label='Cleaned Data', color='blue')

    x_range = np.linspace(min(x), max(x), 1000)
    model_predictions = model_function(x_range, optimal_parameters[0],
                                       optimal_parameters[1])
    ax.plot(x_range, model_predictions, label='Fitted Curve', color='red')

    peak_y_value = model_function(
        optimal_parameters[0], optimal_parameters[0], optimal_parameters[1])

    crossings = find_crossings(x_range, model_predictions, peak_y_value/2)

    if len(crossings) >= 2:
        x_crossings = x_range[crossings]
        y_crossing = peak_y_value/2
        ax.hlines(y=y_crossing, xmin=x_crossings[0], xmax=x_crossings[1],
                  linestyle='-', color='g', label='Half Maximum')

    ax.vlines(x=optimal_parameters[0], ymin=0, ymax=peak_y_value,
              linestyle='--', color='red', label='Resonance mass')
    ax.text(optimal_parameters[0]-2*optimal_parameters[1], peak_y_value,
            f'Resonance Mass: {optimal_parameters[0]:.4g} GeV',
            ha='left', va='top', color='black', fontsize=10)
    ax.text(optimal_parameters[0]-2*optimal_parameters[1], peak_y_value,
            f'FWHM: {2 * optimal_parameters[1]:.4g} GeV',
            ha='left', va='bottom', color='black', fontsize=10)

    ax.legend()
    ax.set_xlabel('Centre-of-mass energy (GeV)')
    ax.set_ylabel('Cross section (nb)')
    plt.savefig('fitted_curve_plot.png', dpi=600)
    plt.show()
    plt.close()


def print_statement(parameters, parameter_uncertainties, lifetime,
                    lifetime_uncertainty, reduced_chi_squared, iteration):
    """
    Display the optimal parameters and other calculated quantities.

    Parameters
    ----------
    parameters : list
        Optimal parameters.
    parameter_uncertainties : tuple
        Uncertainties on parameters.
    lifetime : float
        Lifetime of particle.
    lifetime_uncertainty : float
        Uncertainty on lifetime.
    reduced_chi_squared : float
        Calculated reduced chi-squared from the fit.
    iteration : integer
        Number of iterations it took to remove outliers from the data.
    """
    print("\nOptimal Parameters:")
    print("----------------------")
    print(
        f"Resonance mass: {parameters[0]:.4g} \u00b1"
        f" {parameter_uncertainties[0][0]:.1g} GeVc\u207B\u00B2")
    print(
        f"Resonance width: {parameters[1]: .4g} \u00b1"
        f"{parameter_uncertainties[0][1]:.3f} GeV")
    print(f"Lifetime: {lifetime:.3g} \u00b1 {lifetime_uncertainty:.1g} s")
    print(f"Reduced chi-squared value: {reduced_chi_squared:.3f}")
    print(f"This was completed in {iteration} iterations.")


def main():
    """Handle execution of functions for the Z boson analysis."""
    csvfiles = ['z_boson_data_1.csv', 'z_boson_data_2.csv']

    try:
        loaded_data = read_input_data(*csvfiles)
        cleaned_data = clean_data(
            *loaded_data, remove_outliers=False, z_score_threshold=3)
        combined_data = np.vstack(cleaned_data)
        energy, cross_section, uncertainties = combined_data.T

        (optimal_parameters, covariance, energy, cross_section, uncertainty,
         iteration, lifetime, lifetime_uncertainty) = (
            fit_to_model_function(energy, cross_section, uncertainties))

        plot_data_and_fit(energy, cross_section,
                          uncertainty, optimal_parameters)

        reduced_chi_squared = calculate_reduced_chi_squared(
            cross_section, model_function(energy, *optimal_parameters),
            uncertainty, len(optimal_parameters))

        parameter_uncertainties = np.sqrt(np.diag(covariance)),

        print_statement(optimal_parameters, parameter_uncertainties, lifetime,
                        lifetime_uncertainty, reduced_chi_squared, iteration)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
