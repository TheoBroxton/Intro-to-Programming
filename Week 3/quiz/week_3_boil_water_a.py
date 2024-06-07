# -*- coding: utf-8 -*-
"""
PHYS20161 quiz Clausius Claperyon Relation A

This code calculates the boiling point of water for a given height above sea
level.

Run this code, as is, through the linter and select the correct score on
BlackBoard.

Lloyd Cawthorne 30/08/21
"""
import numpy as np

# SI units

LATENT_HEAT = 40660
GAS_CONSTANT = 8.314
PRESSURE_SEA_LEVEL = 101325
BOILING_POINT_SEA_LEVEL = 100  # Celsius

GRAVITATIONAL_ACCELERATION = 9.81
STANDARD_TEMPERATURE = 273.15  # kelvin
MOLAR_MASS_AIR = 0.02896  # kg/mol


def kelvin_to_celsius(temperature_kelvin):

    return temperature_kelvin - STANDARD_TEMPERATURE


def get_height():

    height = float(input("Enter a height above sea-level in metres: "))

    return height


def pressure_from_height(height, temperature=STANDARD_TEMPERATURE):

    maxwell_factor = np.exp(
        -GRAVITATIONAL_ACCELERATION
        * height
        * MOLAR_MASS_AIR
        / (temperature * GAS_CONSTANT)
    )

    return PRESSURE_SEA_LEVEL * maxwell_factor


def clausius_claperyon_relation(temperature=STANDARD_TEMPERATURE):

    height = get_height()

    pressure = pressure_from_height(height, temperature=temperature)

    new_temperature = 1 / (
        1 / (STANDARD_TEMPERATURE + BOILING_POINT_SEA_LEVEL)
        + GAS_CONSTANT * np.log(PRESSURE_SEA_LEVEL / pressure) / LATENT_HEAT
    )

    return new_temperature - STANDARD_TEMPERATURE
