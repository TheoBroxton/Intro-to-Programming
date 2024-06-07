#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example plot with three additional features: linewidth, color and fontsize
Plots y = 3x from x=0 to 99

PHYS20161 Week 8

Charanjit Kaur 07/11/23
"""

import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(100)
y_values = 3*x_values

fig=plt.figure()
ax=fig.add_subplot(111)

ax.plot(x_values, y_values, linewidth=3, color='red')

ax.set_xlabel('x', fontsize=18)
ax.set_ylabel('y', fontsize=18)
ax.set_title('y=3x', fontsize=18,color='blue')

#plt.savefig('colored_line.pdf')
plt.savefig('colored_line.png', dpi=300)
plt.show()
plt.close()
 

