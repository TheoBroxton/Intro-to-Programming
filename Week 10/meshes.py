#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import numpy as np


def meshes_1(x, y):
    """
    x : array,  y : array
    Returns
    -------
    x_mesh : array of size len(y) by len(x)
    y_mesh : array of size len(y) by len(x)
    """ 
    x_mesh = np.empty((0, len(x)))
    for i, v in enumerate(y):
        x_mesh = np.vstack((x_mesh, x))

    y_mesh = np.empty((0, len(y)))
    for i, v in enumerate(x):
        y_mesh = np.vstack((y_mesh, y))
    y_mesh = np.transpose(y_mesh)
    return x_mesh, y_mesh


def meshes_2(x, y):
    """
    x : array,  y : array
    Returns
    -------
    x_mesh : array of size len(y) by len(x)
    y_mesh : array of size len(y) by len(x)
    """ 
    return np.meshgrid(x, y)


def meshes_3(x, y):
    """
    x : array,  y : array
    Returns
    -------
    x_mesh : array of size len(y) by len(x)
    y_mesh : array of size len(y) by len(x)
    """ 
    dx = x[1]-x[0]
    dy = y[1]-y[0]
    return np.mgrid[slice(np.min(y), np.max(y) + dy, dy),
                    slice(np.min(x), np.max(x) + dx, dx)]


x_values = np.arange(0, 11, 2)  # [0,2,4,6,8,10]
y_values = np.arange(1, 21, 2)  # [1,3,5,7, .... 17,19]

x_mesh_1, y_mesh_1 = meshes_1(x_values, y_values)
print(' ---- mesh 1 ------')
print(x_mesh_1)
print(y_mesh_1)
print('\n')

x_mesh_2, y_mesh_2 = meshes_2(x_values, y_values)
print(' ---- mesh 2 ------')
print(x_mesh_2)
print(y_mesh_2)
print('\n')

y_mesh_3, x_mesh_3 = meshes_3(x_values, y_values)
print(' ---- mesh 3 ------')
print(x_mesh_3)
print(y_mesh_3)
print('\n')


z = x_mesh_1**2 + y_mesh_2**2
print('z')
print(z)
