# -*- coding: utf-8 -*-
"""
PHYS20161 Week 3 Quiz - Cubic Bravais Lattices A

Given the crystal structure, calculates the nearest and nest-nearest neighbour
distances in terms of the edge length.

This code is part of a set where the structure is different in each case.
Examine its flow and select the appropriate flow-chart in BlackBoard.

Lloyd Cawthorne 21/04/21
"""

CRYSTAL_STRUCTURES = ['sc', 'bcc', 'fcc']

STRUCTURE_SET = False

print('What is the structure of your crystal?')

while not STRUCTURE_SET:
    structure = input("Please type 'sc' for simple cubic, 'fcc' for "
                      "face-centred cubic, or 'bcc' for body-centered cubic.\n"
                      )
    for crystal_structure in CRYSTAL_STRUCTURES:
        if structure == crystal_structure:
            STRUCTURE_SET = True

LENGTH_SET = False
print('What is the lattic edge length in Angstom?')
while not LENGTH_SET:
    lattice_edge_string = input('Please enter a number. ')

    if not lattice_edge_string.isalpha():
        LENGTH_SET = True

lattice_edge = float(lattice_edge_string)

if structure == 'sc':
    print('For a simple cubic lattice the nearest neighbour distance is '
          '{0:3.2f} Angstrom and the next-nearest neighbour distance is '
          '{1:3.2f} Angstrom.'.format(lattice_edge, lattice_edge * 2**0.5))

elif structure == 'bcc':
    print('For a body-centred cubic lattice the nearest neighbour distance is '
          '{0:3.2f} Angstrom and the next-nearest neighbour distance is '
          '{1:3.2f} Angstrom.'.format(((3**0.5)/2) * lattice_edge,
                                      lattice_edge))

else:
    print('For a face-centred cubic lattice the nearest neighbour distance is '
          '{0:3.2f} Angstrom and the next-nearest neighbour distance is '
          '{1:3.2f} Angstrom.'.format(lattice_edge / 2**0.5, lattice_edge))
