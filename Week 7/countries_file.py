#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example: reading file example
Prints the contents of countries.txt

PYS20161 Week 7

Charanjit Kaur 30/10/23
"""
countries_file = open('countries_data.txt','r')

list_of_countries = []

for line in countries_file:
    line = line.strip('\n')
    print(line)
    list_of_countries.append(line)
    
countries_file.close()

list_of_countries.sort(reverse = True)

output_file = open('countries_data_upper_case.txt','w')

print('% List of countries in upper case.', file=output_file)

for country in list_of_countries:
    print(country.upper(), file=output_file)

output_file.close()

