# -*- coding: utf-8 -*-
"""
PHYS20161 Week 7 quiz: Intro to Numpy 5

Lloyd Cawthorne 15/06/20

You are given an array 'argument_array' with entries x_i.
The for loop is set up to print a function with these entries f(x_i).

Use the correct function to return the results requested on BB. Then select the
function from the drop-down menu.

"""

import numpy as np

ARGUMENT_ARRAY = np.array([2.43, 1.38, 6.96, 9.49, 8.48, 2.35, 6.17, 7.88,
                           9.39, 1.73, 6.15, 6.32, 3.3, 6.13, 3.32, 8.26,
                           5.95, 7.58, 6.07, 0.16])

function_array = np.cbrt(ARGUMENT_ARRAY)

for index in function_array:
    print('{:3.2f}'.format(index))
