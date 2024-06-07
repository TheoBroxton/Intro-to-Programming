# -*- coding: utf-8 -*-
"""
PHYS20161 Blackbaord quiz

Week 7: Reading & Writing files 3

Lloyd Cawthorne 29/10/19

This program reads in the file 'data3.txt' (it must be saved in the same
directory[folder] as the .py file) performs a calculation, then outputs into
seperate file.

Correct five bugs in the code below then write the correct operation to match
with the given outputs.

"""

import numpy as np

FILE_NAME = 'data3.txt'

# Open data file to be read
input_file = open(FILE_NAME, 'r')

# Empty array to store data
raw_data = np.empty((0, 2))


# Read data line by line and add each pair as an entry to RAW_DATA
for line in input_file:
    entries = line.split(',')
    temp = np.array([])
    temp = np.append(temp, float(entries[0]))
    temp = np.append(temp, float(entries[1]))

    raw_data = np.vstack((raw_data, temp))

input_file.close()
#  Aside: The above line is vital.

# Empty array for resultant calculations

# Perform calculation for each row, you need to code here
first_column = raw_data[:, 0]
second_column = raw_data[:, 1]

results = second_column / first_column

# Open output file to write
output_file = open('output.txt', 'w')

# Print to file
for x in results:
    print('{0:3.2f}'.format(x), file=output_file)

# Close output file
output_file.close()
