# -*- coding: utf-8 -*-
"""
PHYS20161 Week 8 Quiz 1D uncertainty analysis PRACTICE

This code performs a 1D minimised chi square fit on data that describes a
polynomial.

Write some code to read in chi_square_analysis_data_practice_a.txt to begin
with and perform the fit. Then, write some code to find the standard devation
on the coefficient.

You will need to modify the code further to work with
chi_square_analysis_data_practice_b.txt and
chi_square_analysis_data_practice_c.txt.
(Some issues might be hard-coded here!)

Lloyd Cawthorne 25/08/21
"""

import numpy as np
import matplotlib.pyplot as plt

START_VALUE = 3.8
STEP_SIZE = 0.01
TOLERANCE = 0.0001
MAX_ITERATIONS = 100

FILE_NAME = 'chi_square_analysis_data_practice_a.txt'


def is_number(number):
    """
    Checks if number is float. Returns bool
    number (float)
    """
    try:
        float(number)
        return True
    except ValueError:
        return False


def read_data(file_name):
    """
    Reads in data given file name.

    Parameters
    ----------
    file_name : string

    Returns
    -------
    data : np.array of floats
        Data should be in format [x, y, uncertainty on y]
    """
    DATA_OPEN = False

    try:
        input_file = open(FILE_NAME, 'r')
        DATA_OPEN = True

    except FileNotFoundError:
        print('Unable to open file.')

    if DATA_OPEN:
        data = np.zeros((0, 3))
        SKIPPED_FIRST_LINE = False
        for line in input_file:

            if not SKIPPED_FIRST_LINE:
                SKIPPED_FIRST_LINE = True

            else:

                split_up = line.split(',')
                valid = []
                for entry in split_up:
                    valid.append(is_number(entry))
                if all(valid):
                    temp = np.array([float(split_up[0]), float(
                        split_up[1]), float(split_up[2])])

                    data = np.vstack((data, temp))
    input_file.close()

    return data


def function(x, coefficient):
    """
    Function to be fitted
    Parameters
    ----------
    x : float

    coefficient : float

    Returns
    -------
    float
    """

    return np.sin(x) / (coefficient * x + 1)


def chi_square(observation, observation_uncertainty, prediction):
    """
    Returns the chi squared.

    Parameters
    ----------
    observation : numpy array of floats
    observation_uncertainty : numpy array of floats
    prediction : numpy array of floats


    Returns
    -------
    float
    """

    return np.sum((observation - prediction)**2 / observation_uncertainty**2)


def hill_climbing(function, x_minimum=START_VALUE, step=STEP_SIZE):
    """
    Performs 1D hill climbing algorithm with varying step size.

    Parameters
    ----------
    function : function of single argument (float) that returns a float
    x_minimum : float, optional
        The default is START_VALUE.
    step : float, optional
        The default is STEP_SIZE.

    Returns
    -------
    x_minimum : float
        Optimum value of parameter
    minimum : float
        Minimum value of function
    counter : int
        Number of iterations
    """
    difference = 1
    minimum = function(x_minimum)
    counter = 0

    while difference > TOLERANCE:
        counter += 1
        minimum_test_minus = function(x_minimum - step)
        minimum_test_plus = function(x_minimum + step)
        if minimum_test_minus < minimum:
            x_minimum -= step
            difference = minimum - minimum_test_minus
            minimum = function(x_minimum)
        elif function(x_minimum + step) < minimum:
            x_minimum += step
            difference = minimum - minimum_test_plus
            minimum = function(x_minimum)
        else:
            step = step * 0.1

        if counter == MAX_ITERATIONS:
            print('Failed to find solution after {0:d} iterations.'.
                  format(counter))
            break

    return x_minimum, minimum, counter


def find_sigma():
    """


    Returns
    -------
    None.

    """
    coefficient = fitted_coefficient

    while (chi_sq := function(x, coefficient)) < minimum_chi_sq + 1:
        coefficient += STEP_SIZE

    sigma1 = np.abs(coefficient - fitted_coefficient)
    coefficient = fitted_coefficient

    while (chi_sq := function(x, coefficient)) < minimum_chi_sq + 1:
        coefficient -= STEP_SIZE

    sigma2 = np.abs(coefficient - fitted_coefficient)

    return (sigma1 + sigma2)/2


def plot_result(data, result):
    """
    Plots result.

    Parameters
    ----------
    data : numpy array of floats
        Should be in format (x, y, y_uncertainty)
    result : float
        Optimum value for coefficient

    Returns
    -------
    None.

    """

    fig = plt.figure()

    ax = fig.add_subplot(111)

    ax.errorbar(data[:, 0], data[:, 1], yerr=data[:, 2], fmt='o')
    ax.plot(data[:, 0], function(data[:, 0], result))

    ax.set_title('Data and line of best fit')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    plt.show()


# def plot_chi_result(coefficient, chi_squared):
#     """
#     Plots result.

#     Parameters
#     ----------
#     data : numpy array of floats
#         Should be in format (x, y, y_uncertainty)
#     result : float
#         Optimum value for coefficient

#     Returns
#     -------
#     None.

#     """

#     fig = plt.figure()

#     ax = fig.add_subplot(111)

#     ax.plot(, function(data[:, 0], result))

#     ax.set_title('Data and line of best fit')
#     ax.set_xlabel('x')
#     ax.set_ylabel('f(x)')
#     plt.show()


def main():
    """
    Main code for programme. Reads data then performs a minimised chi
    squared fit with 1 sigma estimations. Plots result

    Returns
    -------
    int

    """
    # Extra: return from the main early if the file cannot be found.
    data = read_data(FILE_NAME)

    # hill_climibing() takes an argument of a function with a single variable
    # Using lambda here allows us to define a new function around the
    # chi_square which has the correct format, a single argument: coefficient.

    result = hill_climbing(lambda coefficient:
                           chi_square(data[:, 1], data[:, 2],
                                      function(data[:, 0], coefficient)))

    # For the third data set, you should write some code here to filter the
    # data further.

    plot_result(data, result[0])

    # Write 1 standard deviation estimation here, ideally it should be a
    # function. Best way is to find +/- 1 sigma span, then divide by 2.

    sigma = 0  # placeholder

    print('Results: \n Reduced chi squared: {0:.3f} \n Coefficient: {1:.2f} +'
          '/- {2:.2f} \n Iterations: {3:d}'.format(result[1] / 59, result[0],
                                                   sigma, result[2]))

    return 0


main()
