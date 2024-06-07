# -*- coding: utf-8 -*-
"""
PHYS20161 filter sine data.

Ths code reads in sine data for different angles in degrees then applies a
filter before calculating different quantities.

The data for the sine has some noise.

Use your code from last week to read in the data, then write different filters
before calculating the quantities asked for.

A plotting routine has been provided to assist you.

Lloyd Cawthorne 06/09/21

"""

import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = 'filter_sine_data.txt'
DELIMITER = ','


def function(angle):
    """
    Returns the sine for an angle given in degrees.
    Parameters
    ----------
    angle : float

    Returns
    -------
    float
    """
    return np.sin(np.deg2rad(angle))


def read_data(file_name):
    """
    Reads in data file.

    Extra: Can you make this return 1 if the data file cannot be found?

    Parameters
    ----------
    file_name : string

    Returns
    -------
    2D numpy array of floats
    """
    DATA_OPEN = False

    try:
        input_file = open(FILE_NAME, 'r')
        DATA_OPEN = True

    except FileNotFoundError:
        print('Unable to open file.')

    data = np.zeros((0, 2))
    SKIPPED_FIRST_LINE = False
    for line in input_file:

        if not SKIPPED_FIRST_LINE:
            SKIPPED_FIRST_LINE = True

        else:

            split_up = line.split(',')

            temp = np.array([float(split_up[0]), float(split_up[1])])

            data = np.vstack((data, temp))
    return data


def data_filter(data):
    """

    Returns a subset of the data that satisfies the filter.

    Parameters
    ----------
    data : 2D numpy array of floats

    Returns
    -------
    2D numpy array of floats
    """
    new_data = np.empty([0, 2])

    for entry in data:

        if np.abs(entry[1]) > np.deg2rad(entry[0])/10:

            new_data = np.vstack((new_data, entry))

    return new_data


def plot_data(data):
    """
    Produces a plot of the data.

    Parameters
    ----------
    data : 2D numpy array of floats.

    Returns
    -------
    None.
    """

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data[:, 0], data[:, 1], marker='o', s=4)
    ax.set_title('Plot of data')
    ax.set_xlabel(r'$\theta$ (deg)')
    ax.set_ylabel(r'$\sin (\theta)$')
    plt.show()

    return None


def data_operation(data):
    """
    Performs an operation on the data to yield a quantity. Prints a summary.

    Parameters
    ----------
    data : numpy array of floats

    Returns
    -------
    quantity : float
    """
    # You will need to update this operation.
    quantity = len(data)

    if quantity % 1 == 0:
        print('The value found is {0:d}.'.format(quantity))
    else:
        print('The value found is {0:.3f}.'.format(quantity))
    return quantity


def main():
    """
    Runs the main code.

    Returns
    -------
    int
    """

    data = read_data(FILE_NAME)

    # If the data file cannot be found, this will exit the code early & neatly.
    if np.size(data) == 1:
        return 1
    data = data_filter(data)
    data_operation(data)
    plot_data(data)

    return 0


main()
