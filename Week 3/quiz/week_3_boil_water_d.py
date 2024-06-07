# -*- coding: utf-8 -*-

# PHYS20161 quiz Clausius Claperyon Relation D

import numpy as np

# SI units

L = 40660
GC = 8.314
P = 101325
BP = 100  # Celsius

GA = 9.81
T = 273.15  # kelvin
MM = 0.02896  # kg/mol


def K2C(tk):
    """
    Converts degrees kelvin to degrees celsius

    Parameters
    ----------
    tk : float

    Returns
    -------
    float
    """

    return tk - T


def h():
    """
    Asks user for height in metres.
    Returns
    -------
    float
    """
    return float(input("Enter a height above sea-level in metres: "))


def P_fn(h, t=T):
    """
    Calculates pressure assuming isothermal Maxwell distribution of pressure.

    Parameters
    ----------
    h : foat

    t : float, optional
        DESCRIPTION. The default is T

    Returns
    -------
    float
    Pressure in Pa
    """
    temp = np.exp(-GA * h * MM / (t * GC))

    return P * temp


def ClaClau(t=T):
    """
    Applies Clausius-Claperyon equation for an ideal gas to find boiling point
    at different altitudes. Asks user for height.

    Parameters
     ----------
    t : float, optional
        DESCRIPTION. The default is T.

    Returns
    -------
    float
        Temperature in degrees Celsius

    """
    x = h()

    p = P_fn(x, t=t)

    temp = 1 / (1 / (T + BP) + GC * np.log(P / p) / L)

    return temp - T
