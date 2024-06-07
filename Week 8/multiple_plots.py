#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example plots with mutliple subplots

PHYS20161 Week 8

Original source: Mark Lancaster's code repository.
Last modified: Charanjit Kaur 07/11/23
"""
import numpy as np
import matplotlib.pyplot as plt

def x_to_power_n(x,n):
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

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(x_values, x_to_power_n(x_values,1), linewidth=2.5, linestyle='solid')
ax1.text(2.5, 7.5, '1st plot')

ax2 = fig.add_subplot(222)
ax2.plot(x_values, x_to_power_n(x_values,2), linewidth=2.5, linestyle='dotted')
ax2.text(2.5, 40.0, '2nd plot', rotation = 90)

ax3 = fig.add_subplot(223)
ax3.plot(x_values, x_to_power_n(x_values,3), linewidth=2.5, linestyle='dashed')
ax3.set_xlabel('3rd plot')

ax4 = fig.add_subplot(224)
ax4.plot(x_values, x_to_power_n(x_values,4), linewidth=2.5,linestyle='dashdot')
ax4.set_xlabel('4th plot')

fig.tight_layout(pad=1.0)
plt.show()
plt.close()

