# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:25:00 2023

@author: theob
"""
import numpy as np

# Assuming cleaned_data is a list of arrays
cleaned_data = [np.array([1, 2, 0.1]),
                np.array([2, 3, 0.2]),
                np.array([3, 4, 0.15]),
                np.array([4, 5, 0.3])]

# Combine the arrays vertically
combined_data = np.vstack(cleaned_data)

# Transpose the array and unpack columns
x, y, uncertainties = combined_data.T

print("x:", x)
print("Shape of x:", x.shape)
print("y:", y)
print("uncertainties:", uncertainties)
