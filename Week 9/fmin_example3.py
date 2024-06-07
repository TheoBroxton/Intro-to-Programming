#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find minima: 2 parameter function f(x,y) = x*exp(-x^2-y^2)
PHYS20161 Week 9

Original source: Mark Lancaster's code repository.
Last modified: Charanjit Kaur 15/11/23
"""
import numpy as np
from scipy.optimize import fmin

X_START = 0.0
Y_START = 0.0

def twoparameter_function(xy):
    xv = xy[0]
    yv = xy[1]
    return xv*np.exp(-xv**2 - yv**2)


result = fmin(twoparameter_function, (X_START, Y_START),
              full_output=True, disp=False)
print(result)

print("\nMinimum value at x = {0: .3f}, y = {1: .3f}\n\
Function value at minima = {2: .3f}\n\
Number of iterations = {3:d}\n\
Number of function calls = {4:d}\n\
Error Code = {5:d}"
      .format(result[0][0], result[0][1],
              result[1], result[2], result[3], result[4]))

 
