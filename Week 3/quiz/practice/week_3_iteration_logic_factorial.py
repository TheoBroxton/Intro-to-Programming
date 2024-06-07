# -*- coding: utf-8 -*-
"""
PHYS20161 Week 3 Quiz Iteration Logic Trees - Factorial

Each of the four functions below performs the same task: calculating the
factorial of the given input; however, they run differently. Match each
function to the corresponding logic tree on BlackBoard.

Lloyd Cawthorne 19/08/2021

"""

def factorial_a(x):
    """
    Calculates the factorial of x

    Parameters
    ----------
    x : int

    Returns
    -------
    factorial_result : int
    """

    factorial_result = 1

    for iterator in range(x):
        factorial_result = factorial_result * (x - iterator)

    return factorial_result


def factorial_b(x):
    """
    Calculates the factorial of x

    Parameters
    ----------
    x : int

    Returns
    -------
    factorial_result : int
    """

    iterator = 1

    factorial_result = iterator

    while iterator <= x:

        factorial_result = factorial_result * iterator
        iterator += 1

    return factorial_result


def factorial_c(x):
    """
    Calculates the factorial of x

    Parameters
    ----------
    x : int

    Returns
    -------
    factorial_result : int
    """

    factorial_result = 1

    for iterator in range(1, x + 1):

        factorial_result = iterator * factorial_result

    return factorial_result


def factorial_d(x):
    """
    Calculates the factorial of x

    Parameters
    ----------
    x : int

    Returns
    -------
    factorial_result : int
    """

    factorial_result = 1

    while x > 1:

        factorial_result = factorial_result * x
        x -= 1

    return factorial_result
