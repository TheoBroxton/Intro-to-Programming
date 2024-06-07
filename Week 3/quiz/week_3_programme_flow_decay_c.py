# -*- coding: utf-8 -*-
"""
PHYS20161 Week 3 Quiz - Nuclear decy programme flow C

Given the half-life of a radioactive nucleus and a time input, the code returns
the fraciton of initial nuclei that have not decayed.

This code is part of a set where the structure is different in each case.
Examine its flow and select the appropriate flow-chart in BlackBoard.

Lloyd Cawthorne 17/05/21
"""
import numpy as np

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

print('What is the half-life of the nuclues?')

HALF_LIFE_SET = False

while not HALF_LIFE_SET:

    half_life_string = input('Please enter a time in seconds. ')
    if not half_life_string.isalpha():

        HALF_LIFE_SET = True

half_life_entered = float(half_life_string)

decay_constant = np.log(2) / half_life_entered

time_elapsed = get_time_elapsed()
fraction_remain(decay_constant, time_elapsed, half_life_entered)
