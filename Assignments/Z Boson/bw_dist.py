# -*- coding: utf-8 -*-
"""
Z^0 Boson

Author: r40563tb
"""
import numpy as np
from scipy.optimize import minimize
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def breit_wigner(E, M, Gamma):
    s = E**2
    return (2 * np.sqrt(2) * Gamma * np.sqrt(Gamma**2 + (np.sqrt(s) - M)**2)) / (np.pi * np.sqrt(s))


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

        # Optionally remove outliers based on z-scores
        if remove_outliers:
            z_scores = np.abs(
                (filtered_data - np.mean(filtered_data, axis=0)) / np.std(filtered_data, axis=0))
            # Keep only the rows within the z-score threshold for each column
            filtered_data = filtered_data[(
                z_scores <= z_score_threshold).all(axis=1)]

        cleaned_data.append(filtered_data.astype(float))

    return tuple(cleaned_data)


def model_function(parameters, x):
    """
    Calculate the model prediction.

    Parameters
    ----------
    parameters : list
        Model parameters.
    x : numpy array
        Input values.

    Returns
    -------
    numpy array
        Model predictions.
    """
    return parameters[0] * x + parameters[1]


def objective_function(parameters, x, y):
    """
    Calculate the objective function (sum of squared residuals).

    Parameters
    ----------
    parameters : list
        Model parameters.
    x : numpy array
        Input values.
    y : numpy array
        Actual data values.

    Returns
    -------
    float
        Objective function value.
    """
    y_pred = model_function(parameters, x)
    residuals = y_pred - y
    return np.sum(residuals**2)


def fit_data(x, y, initial_parameters=None):
    """
    Fit the data using the minimize function.

    Parameters
    ----------
    x : numpy array
        Input values.
    y : numpy array
        Actual data values.
    initial_parameters : list, optional
        Initial parameters for the optimization. Defaults to [1.0, 0.0].

    Returns
    -------
    numpy array
        Optimal parameters.
    """
    if initial_parameters is None:
        initial_parameters = [1.0, 0.0]

    result = minimize(objective_function, initial_parameters, args=(x, y))
    optimal_parameters = result.x

    return optimal_parameters


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


def plot_data_and_fit(x, y, optimal_parameters):
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

    ax.errorbar(x, y[:, 0], yerr=y[:, 1], fmt='o',
                label='Original Data with Errorbars', color='blue')

    x_fit = np.linspace(min(x), max(x), 1000)
    y_fit = model_function(optimal_parameters, x_fit)

    ax.plot(x_fit, y_fit, label='Fitted Curve', color='red')
    ax.legend()
    ax.set_xlabel('Centre-of-mass energy (GeV)')
    ax.set_ylabel('Cross section (nb)')

    plt.savefig('fitted_curve_plot.png', dpi=600)
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
            *loaded_data, remove_outliers=True, z_score_threshold=3)
        combined_data = np.vstack(cleaned_data)
        plot_combined_data(combined_data)
        x_data = combined_data[:, 0]
        y_data = combined_data[:, 1:]
        # Fit the data with default initial parameters
        optimal_parameters = fit_data(x_data, y_data[:, 0])

        # Display the optimal parameters
        display_optimal_parameters(optimal_parameters)

        # Plot the data and the fitted curve
        plot_data_and_fit(x_data, y_data, optimal_parameters)

        energy_data = combined_data[:, 0]
        cross_section_data = combined_data[:, 1]
        uncertainties_data = combined_data[:, 2]

        initial_guess = [90, 10]
        fit_params, covariance = curve_fit(
            breit_wigner, energy_data, cross_section_data, p0=initial_guess, sigma=uncertainties_data)

        plt.errorbar(energy_data, cross_section_data,
                     yerr=uncertainties_data, fmt='o', label='Experimental Data')

        plt.plot(energy_data, breit_wigner(energy_data, *fit_params),
                 label='Fit Result', color='red')
        plt.xlabel('Center-of-Mass Energy')
        plt.ylabel('Cross Section')
        plt.legend()
        plt.show()

        # Extract the optimized parameters
        optimized_M, optimized_Gamma = fit_params

        # Print or use the optimized values
        print("Optimized Mass (M):", optimized_M)
        print("Optimized Decay Width (Gamma):", optimized_Gamma)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        # Handle the file not found error
    except ValueError as e:
        print(f"Error: {e}")
        # Handle the value error


if __name__ == "__main__":
    main()
