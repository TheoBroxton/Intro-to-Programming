# -*- coding: utf-8 -*-
"""
Example of if statement

PHYS20161 Week 2

Theo Broxton 30/9/23
"""

NUMBER = float(input('Enter a number: '))

if NUMBER > 100:
    print("That's greater than 100!")
    
elif NUMBER < 10:
    print("That's less than 10")

else: 
    print("That's between 10 and 100")