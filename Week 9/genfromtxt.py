#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example of genfromtxt
Reads in data file and demonstrates basic options in genfromtxt

PHYS20161 Week 9

Charanjit Kaur 15/11/23
"""
import numpy as np

# By default reads data as floats

data_float = np.genfromtxt('test_data.txt', delimiter=',')
print("data_float", data_float, '\n')

# Specifying data to be integers

data_integer = np.genfromtxt('test_data.txt', delimiter=',', dtype='int32')
print("data_integer", data_integer, '\n')

# Using more options in genfromtxt

data = np.genfromtxt('test_data.csv', comments='%', delimiter=',',
                     skip_header=1)
print("data (test_data.csv)", data)


