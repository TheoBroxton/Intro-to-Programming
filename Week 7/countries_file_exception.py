#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example: reading file example
Prints the contents of countries.txt

PYS20161 Week 7

Charanjit Kaur 30/10/23
"""
list_of_countries = []


try:
    countries_file = open('countries_data.txt','r')
    
    for line in countries_file:
        line = line.strip('\n')
        print(line)
        list_of_countries.append(line)
        
    countries_file.close()
except FileNotFoundError as e:
    print(e)
    print('File nor found: check name or folder location')
    
    
    
