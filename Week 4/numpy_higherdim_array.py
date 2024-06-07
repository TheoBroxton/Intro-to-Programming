#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example of higher dimensional arrays

PHYS20161 Week 4 

Charanjit Kaur 23/09/23
"""

import numpy as np

array_1d = np.array([1,2,3])

array_2d = np.array([[1,2,3],[4,5,6]])

array_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                     [[11,12,13],[14,15,16],[17,18,19]],
                     [[21,22,23],[24,25,26],[27,28,29]]])

print("1D array: ", array_1d)
print("2D array: ", array_2d)
print("3D array: ", array_3d)