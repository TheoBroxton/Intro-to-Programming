#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: validation using try and (bare) except

PHYS20161 Week4

Charanjit Kaur 23/09/23
"""

x_string = input("Enter first integer: ")
y_string = input("Enter second integer: ")

try:

    x_int = int(x_string)
    y_int = int(y_string)
    number_div = x_int/y_int
    print('{0}/{1} is {2:.3f}'.format(x_int, y_int, number_div))
          
except:
    print("Something went wrong")
        

