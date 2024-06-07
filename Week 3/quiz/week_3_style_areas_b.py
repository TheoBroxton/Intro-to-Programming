# -*- coding: utf-8 -*-
"""
PHYS20161 week 3 style quiz - Areas of regular polygons B

Lloyd Cawthorne 02/04/20

"""
import numpy as np


def polygon_areas(side_length, max_number_of_sides):
    """"
    Calculates the areas of all polygons from 3 to n sides (int)
    of side-length s (float).
    """
    print('For a side-length of {0:3.1f} cm.'.format(side_length))
    areas = []
    number_of_sides = 3
    while number_of_sides <= max_number_of_sides:
        areas.append((side_length**2 * number_of_sides
                     / (4 * np.tan(np.pi / number_of_sides))))

        number_of_sides += 1

    counter = 3
    for area in areas:
        print('A polygon with {0:d} sides has an area of {1:g} cm^2.'
              .format(counter, area))
        counter += 1

    return None
