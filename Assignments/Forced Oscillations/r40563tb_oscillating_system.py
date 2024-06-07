# -*- coding: utf-8 -*-
"""
PHYS20161 Assignment 1: Forced Oscillations

This code calculates the number of oscillations above a given fractional
intensity and the time taken to complete these oscillations.

The system studied has an amplitude given by
       A(t) = (1 / (A_0 + (A_1 * t**2)) * cos(A_2 * t) .

It requires an input of the frequency of oscillation (float), damping constant
A_1 (float) and a minimum fractional intensity (float).
A_0 is a fixed constant of 2.0 m^-1 .

r40563tb  UID: 11013040
Created: 13/10/23
Last updated: 24/10/23
Submission confirmation number: fa8fa6092ed84ec8ad48b29d084abe71
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters for system
A_0 = 2.0
# This is m^-1 with unicode characters for the superscripts
A_0_UNITS = 'm\u207b\u00b9'
FREQUENCY_UNITS = 'Hz'
A_1_UNITS = 'm\u207b\u00b9s\u207b\u00b2'
A_2_UNITS = 'rad s\u207b\u00b9'


def fractional_intensity(time):
    """
    Calculates the intensity of a forced oscillation whose amplitude is given
    by A(t) = (1 / (A_0 + (A_1 * t**2)) * cos(A_2 * t)
    Outputs the fractional intensity relative to the maximum intensity of
    oscillation

    Parameters
    ----------
    time : float
        Time in seconds of desired amplitude

    Returns
    -------
    Fractional intensity : float
        Fractional intensity of oscillation at given time, in range 0-1

    """
    intensity_maximum = (1/A_0)**2

    intensity = (1/(A_0 + (A_1 * (time)**2)) * np.cos(A_2 * (time)))**2

    fractional_intensity_value = intensity / intensity_maximum

    return fractional_intensity_value


def oscillation_number(frequency):
    """
    Calculates the number of oscillations for which the intensity is above the
    user-defined minimum fractional intensity from an inputted frequency.
    Outputs an integer number of oscillations.

    Parameters
    ----------
    frequency : float
        The frequency of oscillation in Hz

    Returns
    -------
    Oscillation number : integer
        The number of oscillations above a defined fractional intensity

    """
    period = 0.5 * (1 / frequency)
    oscillation_number_value = 1
    maxima_time = period * oscillation_number_value
    while fractional_intensity(maxima_time) > MIN_FRACTIONAL_INTENSITY:
        oscillation_number_value += 1
        maxima_time = period * oscillation_number_value

    return oscillation_number_value - 1


def oscillation_time(oscillation_number_value):
    """
    Calculates the time taken for a specified number of oscillations to occur,
    based on the period of oscillation.

    Parameters
    ----------
    oscillation_number : integer
        The number of oscillations

    Returns
    -------
    oscillation_time : float
        Time in seconds for the number of oscillations to complete

    """
    oscillation_time_value = (oscillation_number_value * PERIOD) + PERIOD / 2

    return oscillation_time_value


def get_valid_float_input_in_range(lower, upper, variable, exclusive=True):
    """
    Takes a user input for a variable's value and validates it, checking that
    it is a float between specified upper and lower bounds.

    Parameters
    ----------
    lower : float
        the lower bound of the range you want the variable to be in
    upper : float
        the lower bound of the range you want the variable to be in
    variable : string
        the name of the variable that should be inputted and validated
    exclusive : boolean
        whether the range is exclusive or not

    Returns
    -------
    user_input : float
        The value for the variable that the user inputted, if it satisfies the
        range and type requirements.

    """
    while exclusive:
        try:
            user_input = float(
                input(f'Enter a value for {variable} between {lower} and'
                      f' {upper}: '))
            if lower < user_input < upper:
                return user_input
            print(
                f'The input must be between {lower} and {upper}. '
                'Please try again.')
        except ValueError:
            print('Your input is invalid. Please enter a valid number.')

    while not exclusive:
        try:
            user_input = float(
                input(f'Enter a value for {variable} from {lower} to'
                      f' {upper}: '))
            if lower <= user_input <= upper:
                return user_input
            print(
                f'The input must be from {lower} to {upper}. '
                'Please try again.')
        except ValueError:
            print('Your input is invalid. Please enter a valid number.')


FREQUENCY = get_valid_float_input_in_range(1, 200, 'frequency', False)
A_1 = get_valid_float_input_in_range(0.1, 50, 'a\u2081')
A_2 = 2 * np.pi * FREQUENCY
MIN_FRACTIONAL_INTENSITY = get_valid_float_input_in_range(
    0, 1, 'minimum fractional intensity')

print('\n\nInput parameters \n----------------')
print(f'A\u2080 = {A_0:.1f} {A_0_UNITS}')
print(f'a\u2081 = {A_1:.1f} {A_1_UNITS}')
print(f'a\u2082 = {A_2:.1f} {A_2_UNITS}')
print(f'Frequency = {FREQUENCY:.1f} {FREQUENCY_UNITS}')
print(f'Minimum fractional intensity = {MIN_FRACTIONAL_INTENSITY}')

PERIOD = 0.5 * (1 / FREQUENCY)
N_OSC = oscillation_number(FREQUENCY)
T_OSC = oscillation_time(N_OSC)

try:
    # Graphical plot
    time_series = np.linspace(0, 1.4 * T_OSC, 1000000)
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(time_series, fractional_intensity(time_series),
            lw=0.5 + (10 / N_OSC) - 5/N_OSC)
    ax.set_title('Forced Oscillations')
    ax.set_xlabel('Time (secs)')
    ax.set_ylabel('Fractional Intensity')
    ax.axhline(MIN_FRACTIONAL_INTENSITY, 0.05, 0.95, c='g', ls='--', lw=1)
    ax.annotate(r'$\mathdefault{I^{f}_{min}}$',
                (0.8*time_series.max(), MIN_FRACTIONAL_INTENSITY+0.03), c='g')
    ax.axvline(T_OSC, 0, 0.75, c='r', ls='--', lw=1)
    ax.annotate(r'$\mathdefault{t_{osc}}$', (0.95 * T_OSC, 0.81), c='r')
    ax.set_ylim(bottom=0)
    plt.savefig('oscillating_system.pdf')
    plt.show()

    # Results printed to user
    print('\nResults\n-------')
    RESULT_MESSAGE = ('The number of oscillations above a fractional intensity'
                      ' of {} is {}, which takes a time of {:.3f} seconds.')
    print(RESULT_MESSAGE.format(MIN_FRACTIONAL_INTENSITY, N_OSC, T_OSC))

except ZeroDivisionError:
    print('\nResults\n-------')
    print(('This system has no oscillations that are above a fractional '
          f'intensity of {MIN_FRACTIONAL_INTENSITY}. This is because the '
           'system is damped too strongly for the intensity to reach the '
           'minimum fractional intensity after an oscillation.'))
