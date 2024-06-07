# -*- coding: utf-8 -*-
"""
Exmaples of lambda
Better use of lambda functions
PHYS20161 Week 8
"""

def power_0(x_variable):
    """
    x_variable :float
    Returns: float
    """
    return x_variable**0


def power_1(x_variable):
    """
    x_variable : float
    Returns : float
    """
    return x_variable**1


def power_2(x_variable):
    """
    x_variable :float
    Returns : float
    """
    return x_variable**2


def power_3(x_variable):
    """
    x_variable :float
    Returns : float
    """
    return x_variable**3


power_list = [power_0, power_1, power_2, power_3]

x_cubed = power_list[3](3.0)

lambda_power_list = [lambda x: 1,
                     lambda x: x,
                     lambda x: x**2,
                     lambda x: x**3]

x_cubed = lambda_power_list[3](3.0)

