#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstrates three different approaches to find the factorial of a number

PHYS20161 Week 3 factorial examples

Original Source: Lloyd Cawthorne's code repository
Last modified: Charanjit Kaur 15/09/23
"""

# ~~~~~~~~~~~~~~~~ Function definitions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def factorial_recursion(number):
    """
    Returns the factorial of a number using recursion
    Parameters
    ----------
    number : int

    Returns : int
    """

    if number <= 1:
        return 1

    return number * factorial_recursion(number-1)


def factorial_while(number):
    """
    Returns factorial using a while loop

    number (int)
    """

    number_factorial = 1

    while number > 1:

        number_factorial = number * number_factorial
        number -= 1

    return number_factorial


def factorial_for(number):
    """
    Returns factorial using a for loop

    number (int)
    """

    number_factorial = 1

    for iterator in range(1, number + 1):

        number_factorial = iterator * number_factorial
        print("iterator", iterator)
        print("number_factorial", number_factorial)        

    return number_factorial


# ~~~~~~~~~~~ Main code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = int(input('x = '))

# X_FACTORIAL = factorial_recursion(X)
# x_factorial = factorial_while(x)
x_factorial = factorial_for(x)

print('{0:d}! = {1:d}'.format(x, x_factorial))






