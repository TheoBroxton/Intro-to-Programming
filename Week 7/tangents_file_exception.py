#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example: reading data. 
Reads in a file containing sin and cos for angles from 0 to 90 degrees and
finds the tangent

PYS20161 Week 7

Original source: Mark Lancaster's code repository.
Last modified: Charanjit Kaur 06/11/23
"""

import numpy as np
tangents = np.array([])


try:
    input_file = open('sine_cosine_data.txt', 'r')
    for line in input_file:
        line_no_return = line.strip('\n')
        line_elements = line_no_return.split()
        
        if line_elements[0] != '%' and len(line_elements) ==3:
            try:
                sine_value = float(line_elements[1])
                cosine_value = float(line_elements[2])
                if cosine_value != 0:
                    tangents = np.append(tangents, sine_value/cosine_value)
            except ValueError as e:
                print("ValueError", e)
            except ZeroDivisionError as e:
                print("ZeroDivisionError", e)
        else:
            print("This line begins with % ignoring it:", line_no_return)
                
    input_file.close()
except FileNotFoundError as e:
    print(e)
    print("File not found: check name and folder location")

print(tangents)
