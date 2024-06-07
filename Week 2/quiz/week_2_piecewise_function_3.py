# -*- coding: utf-8 -*-

"""
PHYS20161 Week 2 quiz - Piecewise function 3

Lloyd Cawthorne 28/05/19

This code computes a piecewise function defined as:

x+5 for -5 <= x < -3

2- exp(-x^2) for -3 <= x < 3

-x+5 for 3 <= x < 5

0 otherwise

Correct the scope (indentation) for it to run correctly.

Once the task is completed can you identify the refactor issues?
Can you fix them?

"""

# Call Exp function
import numpy as np


def function(x_variable):
   """Returns value of function explained in header (float) for a given
input (float).
"""
if -5 <= x_variable <= 5:
    if x_variable < -3:
        first_slope = x_variable + 5.0
        return first_slope
    elif x_variable < 3:
        parabola = 2 - np.exp(-x_variable**2)
        return parabola
    else:
        second_slope = -x_variable + 5
        return second_slope
else:
return 0.0


x_input_string = input("Enter an argument for the function: ")
# Cast input to float
x_input = float(x_input_string)

y_output = function(x_input)
print("y(", x_input, ") = ", y_output)
