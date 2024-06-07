# -*- coding: utf-8 -*-
"""
PHYS20161 Blackboard Quiz Read and compare data cos function

This code reads in data, manipulates it, and compares it to a function.

Fix 5 bugs to get the code working. Once it is working you can answer the main
part of the question (worth 5 marks). To get the remaining 5 marks, you need to
write a function that finds the reduced chi squared for the various phases
given (treat the phases as a degree of freedom).

This question is not negatively marked.

In this code some variables are written as constants (upper case) in accordance
with PEP8. As you can see the majority are not constant and have their values
updated. Could you write these routines in terms of functions instead?

Lloyd Cawthorne 1/11/19

"""
import numpy as np
import matplotlib.pyplot as plt

PHASES = np.array([0, np.pi / 7, np.pi / 4, np.pi / 3, np.pi / 2])


def cos_function(angle, phase_variable):
    """
    computes cos(angle + phi) for angle in degrees and phi in radians.

    angle (float)
    phase_variable (float)
    """
    return np.cos(np.deg2rad(angle) + phase_variable)


def reduced_chi_squared(observed, uncertainties):
    """


    Returns
    -------
    None.

    """
    expected = cos_function(data[:, 0], 1.571)
    chi_squared = np.sum(((observed - expected) / uncertainties) ** 2)
    dof = len(observed) - 1
    return chi_squared / dof


DATA_OPEN = False

try:
    input_file = open('cos_data.txt', 'r')
    DATA_OPEN = True

except FileNotFoundError:
    print('Unable to open file.')

if DATA_OPEN:

    data = np.zeros((0, 3))
    SKIPPED_FIRST_LINE = False
    for line in input_file:
        if not SKIPPED_FIRST_LINE:
            SKIPPED_FIRST_LINE = True

        else:
            split_up = line.split()
            temp = np.array([float(split_up[0]), float(split_up[1]),
                             float(split_up[2])])
            data = np.vstack((data, temp))

    input_file.close()

    angles = np.linspace(np.min(data[:, 0]), np.max(data[:, 0]), 1000)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.errorbar(data[:, 0], data[:, 1], yerr=data[:, 2], fmt='o',
                label='data')
    for phase in PHASES:
        ax.plot(angles, cos_function(angles, phase),
                label=r'\phi = {:4.3f} (rad)'.format(phase))
    ax.legend(bbox_to_anchor=(1.04, 1))
    ax.grid(True, color='grey', dashes=[4, 2])
    ax.set_xlabel(r'\theta (degrees)')
    ax.set_ylabel(r'cos(\theta +\phi)')
    plt.show()

    red_chi_value = reduced_chi_squared(data[:, 1], data[:, 2])
    print(red_chi_value)
