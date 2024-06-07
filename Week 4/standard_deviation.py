#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Standard deviation example

PHYS20161 Week 4

Charanjit Kaur 23/09/23
"""
import numpy as np

def standard_deviation(array):
    """
    Calculates standard deviation of numpy arrays
    Parameters
    ----------
    numpy_array : float

    Returns
    -------
    standard_deviation : float

    """
    average = np.average(array)
    squared_variances = np.power((array - average), 2)
    standard_deviation = np.sqrt(np.sum(squared_variances)/
                                  (array.size - 1))

    return standard_deviation


numpy_array = np.array([1, 4, 6, 8, 4, 11, 6, 8, 7, 5, 6, 8, 16, 14])

print('{:4.3f}'.format(standard_deviation(numpy_array)))
print('{:4.3f}'.format(np.std(numpy_array, ddof=1)))


