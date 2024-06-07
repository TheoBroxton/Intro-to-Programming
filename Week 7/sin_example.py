#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: write sine of angles from 0 to 180 in 2 degree steps to a file

PHYS20161 Week 7

Original source: Mark Lancaster's code repository.
Last modified: Charanjit Kaur 30/10/23
"""

import numpy as np

angles = np.arange(0, 182, 2)
angles_radians = np.deg2rad(angles)
sines = np.sin(angles_radians)

sine_file = open('sine_data.txt', 'w')
print("# angle (degree), sine value", file=sine_file)  # header

for index in range(len(sines)):
    print(angles[index], sines[index])

    print("{0:.2f}, {1:.3f}".format(
        angles[index], sines[index]), file=sine_file)

sine_file.close()


# Can also loop in two other ways ...
for index in enumerate(angles):
    print(index)
    print(angles[index[0]], sines[index[0]])  # index is a tuple 

for index, angle in enumerate(angles):
    print(index)
    print(angle, sines[index])
