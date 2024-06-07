#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic example of plot: 
Plots y = 3x from x=0 to 99

PHYS20161 Week 8

Charanjit Kaur 07/11/23
"""

import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(100)
y_values = 3*x_values

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x_values, y_values)

ax.set_xlabel('x-label (x)')
ax.set_ylabel('y-label (y)')
ax.set_title('Plot title (y=3x)')

plt.savefig('basic_plot.png', dpi=300)
plt.show()
plt.close()
 



