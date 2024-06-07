#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example plot: Simple Example: Data Filtering

PHYS20161 Week 8

Original source: Mark Lancaster's code repository.
Last modified: Charanjit Kaur 08/11/23
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([])
y = np.array([])

file = open('expdata.txt', 'r')
for line in file:
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
print("Size of the two arrays = ", x.size, y.size)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, 'bo', label='Raw data')
x_value = np.linspace(-5.0, 5.01, 1000)
y_value = 2*x_value**2 + 3*x_value + 1
ax.plot(x_value, y_value, 'r-', label=r'Predicted: $2x^2 + 3x+1$')
ax.set_xlabel(r'$x$', fontsize=16)
ax.legend(loc='upper left')
plt.tight_layout()
plt.show()


y_average = np.average(y[np.where(x > 1.0)])
print("Average y value when x > 1.0 is {0:.3f}".format(y_average))

# creates array of predictions same size as x
y_predicted = 2*x**2 + 3*x + 1
outlier_indices = np.where(np.abs(y - y_predicted) > 5.0)
x_subset = x[outlier_indices]
y_subset = y[outlier_indices]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x_value, y_value, 'r-', label=r'Predicted: $2x^2 + 3x+1$')
ax.plot(x_subset, y_subset, 'go', label='Outlier Raw Data')

# Remove outliers from original array using np.delete & plot
x_ok = np.delete(x, outlier_indices)
y_ok = np.delete(y, outlier_indices)
ax.plot(x_ok, y_ok, 'ko', label='Non-Outlier Raw Data')

ax.set_xlabel(r'$x$')
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()
