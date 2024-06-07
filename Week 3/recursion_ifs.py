# -*- coding: utf-8 -*-
"""
PHYS20161 week 3

Example of recursive functions with if statements

Lloyd Cawthorne 10/09/19
"""


def over_x00_statements(input_number, iterator):

    """Performs a series of logic comparisons based on input
       and outputs accordingly.

       input_number (float) or (int)
       iterator (int)"""

    multiple_of_100 = iterator * 100

    if input_number > multiple_of_100:
        print("That's greater than ", multiple_of_100, "!")
        over_x00_statements(input_number, iterator + 1)

    elif input_number < multiple_of_100 + 10:

        print("...but less than ", multiple_of_100 + 10, ".")
    else:

        print("...between ", multiple_of_100 + 10, " and ", iterator * 100,
              ".")
    return None


ITERATOR = 0
NUMBER = float(input('Enter a number: '))

over_x00_statements(NUMBER, ITERATOR)
