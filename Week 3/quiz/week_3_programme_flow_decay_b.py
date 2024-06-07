# -*- coding: utf-8 -*-
"""
PHYS20161 Week 3 Quiz - Nuclear decy programme flow B

Given the half-life of a radioactive nucleus and a time input, the code returns
the fraciton of initial nuclei that have not decayed.

This code is part of a set where the structure is different in each case.
Examine its flow and select the appropriate flow-chart in BlackBoard.

Lloyd Cawthorne 17/05/21
"""
import numpy as np

def get_decay_constant():
    """
    Asks user for half-life (in seconds) validates the input and converts to
    decay constant.

    Returns
    -------
    decay_constant : float
        1 / seconds
    """

    print('What is the half-life of the nuclues?')

    while True:

        half_life_string = input('Please enter a time in seconds. ')
        if not half_life_string.isalpha():

            decay_constant = np.log(2) / float(half_life_string)

            return decay_constant

def get_time_elapsed():
    """
    Asks and validates user input for time in seconds.

    Returns
    -------
    float
    """

    print('How much time has elapsed?')
    while True:
        time_string = input('Please enter a time in seconds. ')
        if not time_string.isalpha():
            return float(time_string)

def fraction_remain(decay_constant, time):
    """
    Calculates percentage of nuclei that remain and prints result.

    Parameters
    ----------
    decay_constant : float
        1 / seconds
    time : float
        seconds

    Returns
    -------
    fraction : float
    """

    fraction = np.exp(-decay_constant * time)

    print('{0:2.0f} % remains of a sample of nuclei with a halflife of {1:.2g}'
          ' seconds after {2:.2g} seconds.'.format(fraction * 100,
                                                   np.log(2) / decay_constant,
                                                   time))
    return fraction

decay_constant_entered = get_decay_constant()
time_elapsed = get_time_elapsed()
fraction_remain(decay_constant_entered, time_elapsed)
