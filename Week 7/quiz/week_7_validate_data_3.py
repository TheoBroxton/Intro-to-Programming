# -*- coding: utf-8 -*-
"""
PHYS20161 Week 7 Read & Validate data 3

Write code to read in and validate the data. The validation should exclude any
row with non-numerical entries or values for y less than zero. A plotting
routine has been provided to assist you.

Find the average of the squared x values, <x^2>, and the average of the y
values.

Lloyd Cawthorne 18/09/21

"""

import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = 'unvalidated_data_3.csv'


def create_plot(data):
    """
    Creates a plot of the data

    Parameters
    ----------
    data : numpy array, [float, float]
        Data should be in order independent variable, dependent variable

    Returns
    -------
    None.

    """

    fig = plt.figure()

    ax = fig.add_subplot(111)

    ax.set_title('Data')
    ax.set_xlabel('x')
    ax.set_ylabel('y(x)')
    ax.scatter(data[:, 0], data[:, 1], s=1)
    plt.show()
    return None


data = np.genfromtxt('unvalidated_data_3.csv', delimiter=',', skip_header=1)
first_column = data[:, 0]
squared_values = first_column ** 2
average_squared = np.mean(squared_values)

second_column = data[:, 1]
second_average = np.mean(second_column)

create_plot(data)


# Main code
