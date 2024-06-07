#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example of functions in if statements.

PHYS20161 Week 2

Original Source: Lloyd Cawthorne's code repository
Last modified: Charanjit Kaur 04/09/23
"""


def over_300_statements(input_number):

    """
    Performs a series of logic comparisons based on input
       and outputs accordingly.

       input_number (float) or (int) 
    """

    if input_number > 400:
        return print("... and greater than 400!")

    elif input_number < 310:
        return print("...but less than 310.")

    else:
        return print("...between 310 and 400")


def over_200_statements(input_number):

    """
    Performs a series of logic comparisons based on input
    and outputs accordingly.

    input_number (float) or (int)
    """

    if input_number > 300:

        print("... and greater than 300!")

        over_300_statements(input_number)

    elif input_number < 210:
        print("...but less than 210.")

    else:
        print("...between 210 and 300")

    return None


def over_100_statements(input_number):

    """
    Performs a series of logic comparisons based on input
    and outputs accordingly.

    input_number (float) or (int) 
    """

    if input_number > 200:

        print("... and greater than 200!")

        over_200_statements(input_number)
        return None

    elif input_number < 110:
        return print("...but less than 110.")

    else:
        return print("...between 110 and 200")


NUMBER = float(input('Enter a number: '))

if NUMBER > 100:
    print("That's greater than 100!")

    over_100_statements(NUMBER)

elif NUMBER < 10:
    print("That's less than 10.")

else:
    print("That's between 10 and 100.")
