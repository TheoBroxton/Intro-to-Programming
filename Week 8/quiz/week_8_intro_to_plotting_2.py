# -*- coding: utf-8 -*-
"""
PHYS20161 Week 8 quiz Intro to matplotlib 2

This code is setup to produce a plot.

Select the correct options on BlackBoard to produce the plot displayed.

Lloyd Cawthorne 29/10/19

"""

import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-np.pi, np.pi, 1000)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Figure 1', fontsize=15, fontname='Times New Roman')
ax.set_xlabel('x', color='r')
ax.set_ylabel('Functions', fontstyle='italic', fontsize=12)
ax.plot(x_values, 5*np.sinc(x_values)**2, label='5 sinc(x)^2', c='black',
        alpha=1)
ax.plot(x_values, 5*np.exp((-x_values**2) / 0.25), label='5 exp(4 x^2)',
        dashes=[8, 2, 4, 2])
ax.grid(True, axis='y', color='black', dashes=[4, 1, 4, 2])
ax.grid(True, axis='x', color='red', linewidth=2, alpha=0.5)
ax.legend(loc='best')

plt.savefig('plot.png', dpi=600)

plt.show()
