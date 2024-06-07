#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: figsize, facecolor, edgecolor
PHYS20161 Week 9
Charanjit Kaur 18/11/23
"""
import numpy as np
import matplotlib.pyplot as plt


def x_to_power_n(x, n):
    """
    Parameters
    ----------
    x : float
    n : int
    Returns
    -------
    float
    """
    return x**n


x_values = np.arange(1, 10, 0.1)

fig = plt.figure(figsize=(6, 3), facecolor='orange',
                 edgecolor='red', linewidth=10)

ax1 = fig.add_subplot(121)
ax1.plot(x_values, x_to_power_n(x_values, 1), linewidth=2.5, linestyle='solid')
ax1.text(2.5, 7.5, '1st plot')
ax1.grid(True)

ax2 = fig.add_subplot(122)
ax2.plot(x_values, x_to_power_n(x_values, 2),
         linewidth=2.5, linestyle='dotted')
ax2.text(2.5, 40.0, '2nd plot', rotation=90)

fig.tight_layout(pad=1.0)
plt.savefig('figsize.png', dpi=300)
plt.show()
plt.close()
