# -*- coding: utf-8 -*-
"""
PHYS20161 Week 2: functions - molecule speed

Debug the three mistakes in the code below.
Once it works, copy the output into Blackboard.

Lloyd Cawthorne 18/02/19

"""
# S.I. units

# import sqrt function
import numpy as np

BOLTZMANN_CONSTANT = 1.38 * pow(10, -23)

MASS = 4.65 * 10**-26
TEMPERATURE = 278


def thermal_energy(temperature):
    """Returns thermal energy (float) for diatomic molecule given temperature
    in kelvin.
    Input:
        temperature (float)
    """

    energy = 1.5 * BOLTZMANN_CONSTANT * temperature
    return energy


def speed_function(mass, energy):
    """Returns speed (float) from kinetic energy
    Input:
        energy (float)
        mass (float)
    """

    speed = np.sqrt(2.0 * energy / mass)
    return speed


molecule_speed = speed_function(MASS, thermal_energy(TEMPERATURE))
print('The speed of an air molecule is', molecule_speed, 'm/s.')
