# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:16:01 2023

@author: theob
"""
import numpy as np


data_float = np.genfromtxt('test_data.txt', delimiter=',')

print("data_float", data_float)

data_int = np.genfromtxt('test_data.txt', dtype='i4')

print("data_int", data_int)


data = np.genfromtxt('test_data.csv', comments='%',
                     delimiter=',', skip_header=1)

print("data", data)
