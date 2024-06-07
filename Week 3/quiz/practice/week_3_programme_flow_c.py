# -*- coding: utf-8 -*-
"""
PHYS20161 Week 3 Quiz - Cubic Bravais Lattices C

Given the crystal structure, calculates the nearest and nest-nearest neighbour
distances in terms of the edge length.

This code is part of a set where the structure is different in each case.
Examine its flow and select the appropriate flow-chart in BlackBoard.

Lloyd Cawthorne 21/04/21
"""

CRYSTAL_STRUCTURES = ['sc', 'bcc', 'fcc']

def get_input():
    """
    Gets crystal structure and edge length from user. Only accepts structures
    listed in CRYSTAL_STRUCTURES.
    Only accepts edge lengths that are numerical and greater than 0.

    Returns
    -------
    structure_entered : sring

    lattice_edge : float
        Angstrom
    """

    print('What is the structure of your crystal?')

    structure_found = False
    while not structure_found:
        structure_entered = input("Please type 'sc' for simple cubic, 'fcc' "
                                  "for face-centred cubic, or 'bcc' for "
                                  "body-centered cubic.\n")
        for crystal_structure in CRYSTAL_STRUCTURES:
            if structure_entered == crystal_structure:
                structure_found = True

    print('What is the lattic edge length in Angstom?')
    length_found = False
    while not length_found:
        lattice_edge_string = input('Please enter a number. ')

        if not lattice_edge_string.isalpha():

            lattice_edge = float(lattice_edge_string)
            length_found = True

    return structure_entered, lattice_edge

def output_message(crystal_structure, length):
    """
    Prints nearest and next-nearest neighbour distances based on crystal
    structure and lattice edge length.

    Parameters
    ----------
    crystal_structure : string

    length : float
        Angstrom.

    Returns
    -------
    None.
    """

    if crystal_structure == 'sc':
        print('For a simple cubic lattice the nearest neighbour distance is '
              '{0:3.2f} Angstrom and the next-nearest neighbour distance is '
              '{1:3.2f} Angstrom.'.format(length, length * 2**0.5))

    elif crystal_structure == 'bcc':
        print('For a body-centred cubic lattice the nearest neighbour distance'
              ' is {0:3.2f} Angstrom and the next-nearest neighbour distance '
              'is {1:3.2f} Angstrom.'.format(((3**0.5)/2) * length, length))

    else:
        print('For a face-centred cubic lattice the nearest neighbour distance'
              ' is {0:3.2f} Angstrom and the next-nearest neighbour distance '
              'is {1:3.2f} Angstrom.'.format(length / 2**0.5, length))

structure, edge_length = get_input()
output_message(structure, edge_length)
