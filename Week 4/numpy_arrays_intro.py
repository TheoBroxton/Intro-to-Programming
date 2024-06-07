#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example of numpy arrays: Creating numpy array, performing some operations, compares two operations using numpy 
and standard arrays (lists)

PHYS20161 Week 4 

Charanjit Kaur 23/09/23
"""

import numpy as np

numpy_array_1 = np.array([1, 2, 3, 4, 5])

print("numpy_array_1", numpy_array_1)

sqrt_numpy_array = np.sqrt(numpy_array_1)
print("sqrt_numpy_array", sqrt_numpy_array)

numpy_array_1 = np.append(numpy_array_1, 6)
print("numpy_array_1", numpy_array_1)

min_value = np.min(numpy_array_1)
print("min_value", min_value)

index_of_min = np.argmin(numpy_array_1)
print("index_of_min", index_of_min)


#Operations using lists and numpy array
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_array = []

for entry in array:
    squared_array.append(entry**2)

numpy_array = np.arange(1, 11)

squared_numpy_array = numpy_array**2

print("squared_array ",squared_array)
print("squared_numpy_array ",squared_numpy_array)