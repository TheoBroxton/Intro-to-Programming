#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example: reading data. 
Reads in a file containing sin and cos for angles from 0 to 90 degrees and
finds the tangent

PYS20161 Week 7

Original source: Mark Lancaster's code repository.
Last modified: Charanjit Kaur 30/10/23
"""

import numpy as np
tangents = np.array([])


input_file = open('sine_cosine_data.txt', 'r')
for line in input_file:
    line_no_return = line.strip('\n')
    line_elements = line_no_return.split()
    
    if line_elements[0] != '%':
        sine_value = float(line_elements[1])
        cosine_value = float(line_elements[2])
        if cosine_value != 0:
            tangents = np.append(tangents, sine_value/cosine_value)
            
    
input_file.close()
print(tangents)


