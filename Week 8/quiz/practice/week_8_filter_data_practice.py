# -*- coding: utf-8 -*-
"""
PHYS20161 filter data PRACTICE.

Ths code reads in data for different angles in degrees then applies a
filter before calculating different quantities.

The data for the function has some noise.

Use your code from last week to read in the data, then write different filters
before calculating the quantities asked for.

A plotting routine has been provided to assist you.

Lloyd Cawthorne 20/08/21

"""

import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = 'filter_practice_data.txt'
DELIMITER = ','


def function(angle):
    """
    Returns sin(x) x / 8 for x given in degrees.
    Parameters
    ----------
    angle : float, degrees

    Returns
    -------
    float
    """
    angle = np.deg2rad(angle)
    return np.sin(angle) * angle / 8


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
    input_file = open('filter_practice_data.txt', 'r')
    for line in input_file:
        #    print(line)
        _line = line.strip('\n')
        if (_line[0] != '%' and len(_line) > 0):
            print(_line)
            print(_line.split())
            try:
                x_data = float(_line.split()[0])
                y_data = float(_line.split()[1])
                x = np.append(x, x_data)
                y = np.append(y, y_data)
            except ValueError as e:
                print(e)
                print("Cannot convert to float ...", _line)

    file.close()
    return data_array


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
    ax.set_ylabel(r'$\sin (\theta) \theta / 8$')
    plt.show()

    return None


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
    # You will need to write filters here.

    return data


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
    quantity = np.average(data[:, 1])

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
