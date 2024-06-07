#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHYS20162 Week 9 example of plotting opacity

Demonstrates plotting with various opacities.
"""

import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(50)
line_values = 2 * x_values
shifted_line_values = line_values + 10

# Generate 50 random integers between 0 and 100
scatter_values = np.random.randint(0, 100, 50)

plt.figure()
plt.title('Examples of alpha', fontsize=16)

# set marker size, s, proportional to value
plt.scatter(x_values, scatter_values, s=2 * scatter_values, alpha=0.7,
            label='Scatter')
plt.plot(x_values, line_values, c='k', label='No alpha', linewidth=4)

plt.plot(x_values, shifted_line_values, c='k',alpha=0.5, 
         label='Alpha = 0.5',linewidth=4)

plt.legend(fontsize=16)
plt.savefig('alpha.png', dpi=300)
plt.show()
