# -*- coding: utf-8 -*-
"""
PHYS20161 Week 7 quiz: find off set 3

This code reads in data and finds the offset according to the polynomial
defined.

It does this by minimising the variance between the data and the model given
some initial parameters.

Lloyd Cawthorne 08/04/22

"""

import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = 'polynomial_data_3.csv'

STEP = 0.1
TOLERANCE = 1
STARTING_OFFSET = 0


def polynomial(x_variable, offset_variable):
    """
    Returns -1.5 * x^3 + 4 x + offset

    x (float)
    offset_variable (float)
    """
    return -1.5 * x_variable**3 + 4 * x_variable + offset_variable


def is_float(number):
    """Checks if input is valid

    Returns True if number is float.
    """

    try:
        float(number)
        return True

    except TypeError:
        return False


input_file = open(FILE_NAME, 'r')

data = np.zeros((0, 2))

for line in input_file:

    split_up = line.split(',')
    if is_float(split_up[0]) and is_float(split_up[1]):
        temp = np.array([float(split_up[0]), float(split_up[1])])
        data = np.vstack((data, temp))

offset = STARTING_OFFSET
difference = np.sum((data[:, 1] - polynomial(data[:, 0], offset))**2)


while difference > TOLERANCE:

    comparison_0 = np.sum((data[:, 1] - polynomial(data[:, 0], offset))**2)

    comparison_1 = np.sum((data[:, 1] - polynomial(data[:, 0],
                                                   offset + STEP))**2)

    comparison_2 = np.sum((data[:, 1] - polynomial(data[:, 0],
                                                   offset - STEP))**2)

    if comparison_0 > comparison_1:
        difference = comparison_0 - comparison_1
        offset += STEP

    elif comparison_0 > comparison_2:
        difference = comparison_0 - comparison_2
        offset -= STEP
    else:
        print('Failed to reach desired precision.')
        break


print('The fitted offset is {:g}.'.format(offset))

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title('Fitted function against data')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.scatter(data[:, 0], data[:, 1])
ax.plot(data[:, 0], polynomial(data[:, 0], offset), c='black')
plt.show()
