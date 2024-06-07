#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SciPy Example: quad function

PHYS20161 Week 9

"""
import numpy as np
from scipy.integrate import quad

def exponential_function(x_variable):
    return np.exp(np.cos(-2 * x_variable * np.pi)) + 3.2

def parabola(x_variable):
    """
    x_variable: float
    Returns: float(x^4 + 4x^2 + 10)
    
    """
    return x_variable**4 + 4. * x_variable**2 + 10.

# call quad to integrate function(parabola) from -2 to 2
result1, error1 = quad(parabola, -2, 2)

print("Numerical result (parabola function): {:.3f} +/- {:.2g}"
      .format(result1, error1))

# call quad to integrate function(exponential_function) from -2 to 2
result2, error2 = quad(exponential_function, -2, 2)

print("Numerical result (exponential_function) {:.3f} +/- {:.2g}"
      .format(result2, error2))

