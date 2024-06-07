#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import numpy as np
import matplotlib.pyplot as plt


def function(x, y):
    return x**2 + y**2


x_values = np.arange(0, 11, 2)  # [0,2,4,6,8,10]
y_values = np.arange(1, 21, 2)  # [1,3,5,7, .... 17,19]

x_mesh, y_mesh = np.meshgrid(x_values, y_values)


fig = plt.figure()
ax = fig.add_subplot(111)
contour_plot = ax.contour(x_mesh, y_mesh, function(x_mesh, y_mesh), 5)
ax.clabel(contour_plot, fontsize=12, colors='r')
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('y',fontsize=14)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
contour_plot = ax.contour(x_mesh, y_mesh, function(x_mesh, y_mesh), [81, 225])
ax.clabel(contour_plot, fontsize=12, colors='r')
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('y',fontsize=14)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
contour_plot_filled = ax.contourf(x_mesh, y_mesh, function(x_mesh, y_mesh), 5)
fig.colorbar(contour_plot_filled)
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('y',fontsize=14)
plt.show()







