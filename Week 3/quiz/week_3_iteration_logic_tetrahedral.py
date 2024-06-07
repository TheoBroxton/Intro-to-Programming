# -*- coding: utf-8 -*-
"""
PHYS20161 Week 3 Quiz - Iterarion Logic: Tetrahedral Numbers

Each of the four functions below performs the same task: finding the
tetrahedral number less than or equal to the input given. However, they run
differently. Match each function to the corresponding logic tree on BlackBoard.

See https://en.wikipedia.org/wiki/Tetrahedral_number for a definition of these
numbers.

In all cases, input number must be greater than or equal to 1.

Lloyd Cawthorne 31/08/2021
"""


def tetrahedral_a(number):
    """
    Finds the tetrahedral number less than or equal to number.

    Parameters
    ----------
    number : int
    Must be 1 or greater.

    Returns
    -------
    int
    """
    tetrahedral_number = 0

    for iterator_1 in range(number + 1):
        triangular_number = 0

        for iterator_2 in range(iterator_1):
            triangular_number += iterator_2

        tetrahedral_number += triangular_number

        if tetrahedral_number > number:
            return tetrahedral_number - triangular_number

    return 1


def tetrahedral_b(number):
    """
    Finds the tetrahedral number less than or equal to number.

    Parameters
    ----------
    number : int
    Must be 1 or greater.

    Returns
    -------
    int
    """
    tetrahedral_number = 0

    test = 0
    iterator = 0

    while test <= number:
        tetrahedral_number = test

        iterator += 1
        test += iterator * (iterator + 1) // 2


    return tetrahedral_number


def tetrahedral_c(number):
    """
    Finds the tetrahedral number less than or equal to number.

    Parameters
    ----------
    number : int
    Must be 1 or greater.

    Returns
    -------
    int
    """
    tetrahedral_number = 0

    test = 0


    for iterator in range(number + 1):
        tetrahedral_number = test

        iterator += 1
        test += iterator * (iterator + 1) // 2
        if test > number:
            return tetrahedral_number


def tetrahedral_d(number):
    """
    Finds the tetrahedral number less than or equal to number.

    Parameters
    ----------
    number : int
    Must be 1 or greater.

    Returns
    -------
    int
    """
    iterator = 0

    test = 0

    while test <= number:

        tetrahedral_number = test
        test = iterator * (iterator + 1) * (iterator + 2) // 6

        iterator += 1

    return tetrahedral_number
