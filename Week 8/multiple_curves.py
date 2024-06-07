#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example plot: more than 1 curve and legend 

PHYS20161 Week 8

Charanjit Kaur 07/11/23
"""

import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(1,5)
y1_values = 3*x_values
y2_values = 3*x_values**2

fig=plt.figure()
ax=fig.add_subplot(111)

ax.plot(x_values, y1_values, linewidth=3, color='r', label="3x")
ax.plot(x_values, y2_values, linewidth=3, color='b', label="3x^2")
ax.set_xlabel('x-label',fontsize=16)
ax.set_ylabel('y-label',fontsize=16)

ax.legend(loc='upper left')

plt.show()
plt.close()
 


