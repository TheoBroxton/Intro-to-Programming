# -*- coding: utf-8 -*-
"""
PHYS20161 Week 3 Quiz - Nuclear decy programme flow A

Given the half-life of a radioactive nucleus and a time input, the code returns
the fraciton of initial nuclei that have not decayed.

This code is part of a set where the structure is different in each case.
Examine its flow and select the appropriate flow-chart in BlackBoard.

Lloyd Cawthorne 17/05/21
"""
import numpy as np

def get_half_life():
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

            return float(half_life_string)

def halflife_to_decay_constant(half_life):
    """
    Returns decay constant from half-life.

    Parameters
    ----------
    half_life : float

    Returns
    -------
    float
        Inverse units to half-life entered.

    """

    return np.log(2) / half_life

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

def fraction_remain(decay_constant_variable, time, half_life):
    """
    Calculates percentage of nuclei that remain and prints result.

    Parameters
    ----------
    decay_constant_variable : float
        1 / seconds
    time : float
        seconds
    half_life : float
        seconds

    Returns
    -------
    fraction : float
    """

    fraction = np.exp(-decay_constant_variable * time)

    print('{0:2.0f} % remains of a sample of nuclei with a halflife of {1:.2g}'
          ' seconds after {2:.2g} seconds.'.format(fraction * 100,
                                                   half_life,
                                                   time))
    return fraction

half_life_entered = get_half_life()
decay_constant = halflife_to_decay_constant(half_life_entered)
time_elapsed = get_time_elapsed()
fraction_remain(decay_constant, time_elapsed, half_life_entered)
