#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: Demonstrates for loops by printing 0 to 5. 

PYS20161 Week 3 

Charanjit Kaur 15/09/23
"""

ARRAY = [0, 1, 2, 3, 4, 5]

for element in ARRAY:
    print(element)

print('For loop terminated')



for element in range(1, 6, 2):
    print(element)

print('This is an example of the range function- start inclusive, end exclusive. It counts 0 as the first element by default.')