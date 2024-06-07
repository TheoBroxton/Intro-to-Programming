# -*- coding: utf-8 -*-
"""
PHYS20161 Week 2 Logic Tree 1 A

This code asks the user for a number then makes a series of statements based
on its value.

Match the code to the correct logic tree on BlackBoard.

Lloyd Cawthorne 29/06/21
"""

number = float(input("Enter a number: "))

if number.is_integer():

    if number % 2 == 0:
        print('The number is even.')

    else:
        print("The number is odd.")

        if number % 3 == 0:

            print('It is divisible by 3.')

elif 10 * number % 1 == 0:
    print('It has one decimal figure.')

elif 100 * number % 1 == 0:
    print('It has two decimal figures.')

else:
    print('It has more than two decimal figures.')
