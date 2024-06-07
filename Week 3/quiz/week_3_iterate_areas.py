# -*- coding: utf-8 -*-
"""
PHYS20161 week 3 quiz iterate areas

This code finds and prints the area given an array of lengths.
It also showcases some array operations.

Correct three errors then select the appropriate answers on BlackBoard.

Can you find and correct the convetion warning?

Lloyd Cawthorne 23/09/19

"""

# Arbitrary units

LENGTHS = [0.1, 2.6, 3.5, 4.6, 5.389, 6.2, 7.7, 8.0, 9.8]

#  Declare an empty array with the same length as 'LENGTHS'
areas = [0] * len(LENGTHS)

for i in range(len(LENGTHS)):

    # Overwrite each element of AREAS with desired calculation
    areas[i] = LENGTHS[i]**2
    print('The area of length {0:1d} is {1:4.2f}.'.format(i, areas[i]))
