# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:43:34 2023

@author: theob
"""

my_file = open('my_file.txt', 'w')

my_string = 'hello world 2'
my_file.write(my_string)


print(my_string, file=my_file)
my_file.close()
