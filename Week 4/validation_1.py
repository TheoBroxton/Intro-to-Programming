# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:14:38 2023

@author: theob
"""

x_string = input("Enter first integer: ")
y_string = input("Enter second integer: ")


if (x_string.isnumeric() and y_string.isnumeric()):

    x_int = int(x_string)
    y_int = int(y_string)
    
    
    
    if y_int != 0:
    
        number_div = x_int/y_int
        
        print('{0}/{1} is {2:.3f}'.format(x_int, y_int, number_div))
    
    else:
        print('Denominator should be non-zero')
        
else:
    print("One of the inputs is non-numeric")