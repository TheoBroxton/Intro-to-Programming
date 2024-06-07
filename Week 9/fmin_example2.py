#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find mamima of a function using fmin

PHYS20161 Week 9

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin

X_START = -1.5

def parabola(x_variable):
    """
    x_variable: float
    Returns: float(x^4 + 4x^2 + 10)
    
    """
    return -2*x_variable**4 - 4 * x_variable**2 + 5 * x_variable + 10

def negative_parabola(x_variable):
    """
    """
    return -1.0*parabola(x_variable)

result = fmin(negative_parabola, X_START, full_output=True, disp=False)
#result = fmin(-parabola, X_START, full_output=True, disp=False)
#result = fmin(lambda x: -parabola(x), X_START, full_output=True, disp=False)

print(result)

print("\nMaximum value at x = {0: .3f}\n\
Function value at maxima = {1: .3f}\n\
Number of iterations = {2:d}\n\
Number of function calls = {3:d}\n\
Error Code = {4:d}"
      .format(result[0][0], -1.0*result[1], result[2], result[3], result[4]))

x_values = np.linspace(-2, 2, 100)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x_values, parabola(x_values), 'r-')
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('f(x)', fontsize=14)
ax.scatter(result[0][0], -1.0*result[1], label='Maxima', color='b')
plt.legend(loc='upper left', shadow=True, edgecolor='purple')
plt.show()

