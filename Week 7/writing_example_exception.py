#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: Writing files

PYS20161 Week 7

Charanjit Kaur 06/11/23
"""

try:
    my_file = open('data/my_file.txt', 'w')
    my_file.write('hello world')
    my_file.close()
except FileNotFoundError as e:
    print(e)
    print('Error: check your folder name - does it exist?')



#my_file = open('my_file.txt', 'w')
#my_string = 'hello world 2'
#my_file.write(my_string)
#my_file.close()


#my_file = open('my_file.txt', 'w')
#my_string = 'hello world 3'
#print(my_string, file=my_file)
#my_file.close()



