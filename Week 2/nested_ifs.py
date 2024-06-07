#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example of nested if statements

PHYS20161 Week 2

Original Source: Lloyd Cawthorne's code repository
Last modified: Charanjit Kaur 04/09/23
"""

NUMBER = float(input('Enter a number: '))

if NUMBER > 100:
    print("That's greater than 100!")

    if NUMBER > 200:
        print("... and greater than 200!")

        if NUMBER > 300:
            print("... and greater than 300!")

            if NUMBER > 400:
                print("... and greater than 400!")

            elif NUMBER < 310:
                print("...but less than 310.")

            else:
                print("...between 310 and 400")

        elif NUMBER < 210:
            print("...but less than 210.")

        else:
            print("...between 210 and 300")

    elif NUMBER < 110:
        print("...but less than 110.")

    else:
        print("...between 110 and 200")

elif NUMBER < 10:
    print("That's less than 10.")

else:
    print("That's between 10 and 100.")
