#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example plot: using latex symbols and format in legend

PHYS20161 Week 8

Original source: Mark Lancaster's code repository.
Last modified: Charanjit Kaur 08/11/23
"""

import numpy as np
import matplotlib.pyplot as plt


def gaussian(x_variable, mean, standard_deviation):
    """
    Parameters
    ----------
    x_variable : float
    mean : float
    standard_deviation : float

    Returns
    -------
    Float: value of gaussian at x_variable centred over mean 
    with standard deviation

    """
    normalisation = 1.0/(2 * standard_deviation*np.sqrt(np.pi))
    exponent= -(x_variable-mean)**2/(2*standard_deviation**2)
    
    return normalisation*np.exp(exponent)

x_values = np.arange(-2.7, 2.7, 0.01)
mean = np.array([0.0, 1.0, 0.5, -0.5, -1.0])
sigma = np.array([0.1, 0.2, 0.6, 0.3, 0.4])

colors = ['red','green', 'blue', 'cyan', 'black']

fig = plt.figure()
ax = fig.add_subplot(111)

for i in np.arange(0, len(mean)):
    y_values = gaussian(x_values, mean[i], sigma[i])
    legend_label=r'$\mu$={0:.1f}, $\sigma$ ={1:.1f}'.format(mean[i], sigma[i])
    ax.plot(x_values, y_values, color=colors[i], label= legend_label)

ax.legend(loc='upper left')
ax.set_title(r'Gaussians with different $\mu$ and $\sigma$')

plt.show()
plt.close()


