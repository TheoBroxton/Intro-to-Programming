# -*- coding: utf-8 -*-
"""
PHYS20161 week 3 style quiz - Areas of regular polygons A

This code calculates the areas of a regular polygons. Given a max number of
sides its side-length, it calculates the areas of all shapes in that range,

Lloyd Cawthorne 02/04/20

"""
import numpy as np


def a_poly(s, n):
    """"
    Calculates the areas of all polygons from 3 to n sides (int)
    of side-length s (float).
    """
    print('For a side-length of {0:3.1f} cm.'.format(s))

    n_temp=3
    while n_temp<=n:
        area=s**2*n_temp/(4*np.tan(np.pi/n_temp))

        print('A polygon with {0:d} sides has an area of {1:g} cm^2.'
              .format(n_temp, area))
        n_temp+=1

    return None
