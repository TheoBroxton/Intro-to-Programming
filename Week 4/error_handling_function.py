#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finds routes of quadratic equation.
Showcases error handling using try and except.

PHYS20161 Week 4 

Original Source: Lloyd Cawthorne's code repository
Last modified: Charanjit Kaur 23/09/23
"""

def quadratic_solutions(a_coefficient, b_coefficient, c_coefficient):
    """
    Solves ax^2 + bx + c = 0
    Outputs two possible results
    Parameters
    ----------
    a_coefficient : float
    b_coefficient : float
    c_coefficient : float

    Returns
    -------
    The two solutions as floats if they exist, else None

    """
    
    try:
        sqrt_argument = b_coefficient**2 - 4 * a_coefficient * c_coefficient
        if sqrt_argument < 0:
            print('No real solutions.')
            return None, None

        solution_1 = ((-b_coefficient + sqrt_argument**0.5)
                      / (2. * a_coefficient))
        solution_2 = ((-b_coefficient - sqrt_argument**0.5)
                      / (2. * a_coefficient))
        print('Solutions are {0:.2f} and {1:.2f}.'.
              format(solution_1, solution_2))
        return solution_1, solution_2

    except TypeError as e:
        print('TypeError', e)
        print('Make sure input coefficients are all floats.')
        return None, None
    except ZeroDivisionError as e:
        print('ZeroDivisionError', e)
        print('Make sure a_coefficient is not zero.')
        return None, None
