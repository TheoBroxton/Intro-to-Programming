# -*- coding: utf-8 -*-
"""
PHYS20161 Order Functions Quiz - Bragg diffraction

Lloyd Cawthorne 06/04/21

This code calculates angle of incident X-rays on a simple cubic crystal to
observe constructive interference.

Three functions are presented below where the docstrings and function names are
intentionally unclear for the purpose of this task. The code given is correct
and you do not need to change it.

Interpret the functions and select the correct order they need to be called on
BlackBoard. E.g.

function_a()
function_c()
function_b()

Check this by writing the main code below these definitions. You
might need to inlude input variables [e.g. function_a(variable)] and store the
output as a variable[e.g. output = function_b()] or both.
A wavelength of the order 1 Angstrom will return sensible results.
"""
# Import libraries needed for math functions
import numpy as np

# Constants
INTERATOMIC_DISTANCE = 4.123 # Angstrom


# Function definitions

def function_a(wavelength):

    sin_angle = wavelength / (2 * INTERATOMIC_DISTANCE)
    angle_radians = np.arcsin(sin_angle)

    return angle_radians

def function_b():

    wavelength_string = input('What is the wavelength of the incident light in'
                              ' angstroms? ')
    wavelength = float(wavelength_string)

    return wavelength

def function_c(angle_radians):

    angle_degree = np.rad2deg(angle_radians)

    print('Light scattered at ', angle_degree, ' degrees will constructively'
          ' interfere.')

    return None


# Write main code below here.
