# -*- coding: utf-8 -*-
"""
PHYS20161 Week 8 quiz Intro to matplotlib PRACTICE

This code is setup to produce a plot of Fourier Series of a sawtooth wave.
http://mathworld.wolfram.com/SawtoothWave.html
http://mathworld.wolfram.com/FourierSeriesSawtoothWave.html

Select the correct options on BlackBoard to produce the plot displayed.

Lloyd Cawthorne 29/10/19

"""

import matplotlib.pyplot as plt
import numpy as np

# Constants

NUMBER_OF_TERMS = 6  # number of terms in fourier series
PERIOD = 2


def sawtooth(x_variable, period_variable, amplitude=1):
    """
    Outputs a sawtooth that that starts at origin,
    with period and amplitude as given.

    x_variable (float)
    period_variable (float)
    amplitude(float) [default =1]
    """

    return (amplitude * (x_variable / period_variable
                         - np.floor(x_variable / period_variable)))


def sine_terms(x_variable, period_variable, index):
    """
    Returns sine terms for a given index for a fourier series of a
    sawtooth wave.

    x_variable (float)
    period_variable (float)
    index (int)
    """
    return ((1 / index)
            * np.sin(2 * index * np.pi * x_variable / (period_variable)))


def fourier_sawtooth(x_variable, period_variable, order, amplitude=1):
    """
    Outputs a fourier series representing a sawtooth wave upto a given order
    in the summation that that starts at origin, with period and amplitude as
    given.

    x_variable (float)
    period_variable (float)
    order (int)
    amplitude(float) [default = 1]
    """
    terms = 0

    if order > 0:
        # As plot routine iterates over x axis, need to be careful how we
        # iterate over sum of terms
        indices = np.arange(1, order + 1)
        for index in indices:
            terms = terms + sine_terms(x_variable, period_variable, index)

    # return amplitude * (0.5 - 1/np.pi * np.sum(terms))
        return amplitude * (0.5 - 1 / np.pi * terms)

    # If we return a constant value, need to ensure this is the same
    # dimension as array for plotting. Example of an edge case that needs
    # attention
    return np.full(len(x_variable), amplitude / 2)


# Plot creation

x_values = np.linspace(-3.5, 3.5, 1000)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title('Sawtooth and Fourier approximation upto {:d} terms'
             .format(NUMBER_OF_TERMS),
             fontname='Times New Roman', fontsize=16)
ax.set_xlabel('x', fontstyle=None)
ax.set_ylabel('y(x)')
ax.plot(x_values, sawtooth(x_values, PERIOD), label='sawtooth(x)', c='black',
        alpha=0.5)
ax.plot(x_values, fourier_sawtooth(x_values, PERIOD, NUMBER_OF_TERMS),
        label='Fourier approx.', color='purple')
ax.set_ylim(-0.25, 1.25)
ax.set_yticks(np.arange(-0.25, 1.5, 0.25))
ax.set_xlim(-3.5, 3.5)
ax.grid(True, color='grey', dashes=[4, 2])
ax.legend(loc='lower center', ncol=2)

plt.savefig('plot.png', dpi=300)
plt.show()
