# -*- coding: utf-8 -*-
"""
PHYS20161 quiz Clausius Claperyon Relation B

This code calculates the boiling point of water for a given height above sea
level.

Run this code, as is, through the linter and select the correct score on
BlackBoard.

Lloyd Cawthorne 30/08/21
"""
import numpy as np

# SI units

latent_heat = 40660
gas_constant = 8.314
pressure_sea_level = 101325
boilinb_point_sea_level = 100 # Celsius

gravitational_acceleration = 9.81
standard_temperature = 273.15 # kelvin
molar_mass_air = 0.02896 # kg/mol



def kelvin_to_celsius(temperature_kelvin):
    """
    Converts degrees kelvin to degrees celsius

    Parameters
    ----------
    temperature_kelvin : float

    Returns
    -------
    float
    """

    return temperature_kelvin - standard_temperature

def get_height():
    """
    Asks user for height in metres.
    Returns
    -------
    height : float
    """

    height = float(input('Enter a height above sea-level in metres: '))

    return height

def pressure_from_height(height, temperature=standard_temperature):
    """
    Calculates pressure assuming isothermal Maxwell distribution of pressure.

    Parameters
    ----------
    height : foat

    temperature : float, optional
        DESCRIPTION. The default is standard_temperature.

    Returns
    -------
    float
        Pressure in Pa

    """

    maxwell_factor = np.exp(- gravitational_acceleration * height * molar_mass_air
                            / (temperature * gas_constant))

    return pressure_sea_level * maxwell_factor


def clausius_claperyon_relation(temperature=standard_temperature):
    """
    Applies Clausius-Claperyon equation for an ideal gas to find boiling point
    at different altitudes. Asks user for height.

    Parameters
    ----------
    temperature : float, optional
        DESCRIPTION. The default is standard_temperature.

    Returns
    -------
    float
        Temperature in degrees Celsius

    """

    height = get_height()

    pressure = pressure_from_height(height, temperature=temperature)

    new_temperature = 1 / (1 / (standard_temperature + boilinb_point_sea_level)
                           + gas_constant * np.log(pressure_sea_level
                                                   / pressure)
                           / latent_heat)

    return new_temperature - standard_temperature
