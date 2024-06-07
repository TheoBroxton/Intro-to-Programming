# -*- coding: utf-8 -*-
"""
PHYS20161 Week 7 Quiz: Newton Raphson 1

Example of implementing Newton Raphson to find root of 3x^2 - e^-x

Correct the bugs, then find the answers requested on BlackBoard.

"""

import numpy as np
import matplotlib.pyplot as plt

# Initial parameters

X_START = -2

TOLERANCE = 0.01

#  Function definitions


def function(x_variable):
    """Returns 3x^2 - e^-x
    x (float)
    """
    return 3 * x_variable**2 - np.exp(-x_variable)


def derivative(x_variable):
    """Returns 6 x + e^-x, derivative of 3x^2 - e^-x
    x_variable (float)
    """
    return 6 * x_variable + np.exp(-x_variable)


def next_x_function(previous_x):
    """
    Returns next value for x according to algorithm

    previous_x (float)

    """

    return previous_x - function(previous_x) / derivative(previous_x)


def newton_raphson(x_start=X_START, tolerance=TOLERANCE,
                   next_x=next_x_function):
    """Iterates Newton Raphson algorithm until difference between succesive
        solutions is less than tolerance.
        Args:
            x_start: float, kwarg
            tolerance: float, kwarg
            next_x: function returning float, kwarg
        Returns:
            x_root: float
            counter: int
        """
    # set up parameters
    difference = 1
    counter = 0
    x_root = x_start

    # Repeatedly find x_n until the tolerance threshold is met.
    while difference > tolerance:

        counter += 1

        x_test = x_root
        x_root = next_x(x_root)

        difference = np.abs(x_test - x_root)

    return x_root, counter


# Main code

x_values = np.linspace(-10, 5, 100000)

x_solution, iterations = newton_raphson()

# Final plot

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.plot(x_values, function(x_values))
ax.plot(x_values, 0 * x_values, c='grey', dashes=[4, 4])
ax.scatter(x_solution, function(x_solution), c='k', label='x_root')

ax.scatter(X_START, function(X_START), c='red', label='x_0')

ax.set_xlim(-5, 2)
ax.set_ylim(-4, 8)
ax.legend()
plt.show()

print('Root = {:.3f}'.format(x_solution))
print('This took {:d} iterations'.format(iterations))
