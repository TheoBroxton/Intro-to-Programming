# -*- coding: utf-8 -*-
"""
PHYS20161 Blackboard Quiz week 8 Read and compare data function PRACTICE

This code reads in data, manipulates it, and compares it to a function.

Fix 5 bugs to get the code working. Once it is working you can answer the main
part of the question (worth 5 marks). To get the remaining 5 marks, you need to
write a function that finds the reduced chi squared for the various phases
given (treat the phases as a degree of freedom).

This question is not negatively marked.

Lloyd Cawthorne 1/11/19

"""
import numpy as np
import matplotlib.pyplot as plt

PHASES = np.array([0, np.pi / 6, np.pi / 3, np.pi / 2, np.pi])


def function(angle_variable, phase_variable):
    """
    computes 3 cos(angle + phi)^2 sin(angle+phi) for angle in degrees and phi
    in radians  (float).

    angle_variable (float)
    phase_variable (float)
    """
    return (3 * np.cos(np.deg2rad(angle_variable) + phase_variable)**2
            * np.sin(np.deg2rad(angle_variable) + phase_variable))


DATA_OPEN = False

try:
    input_file = open('week_8_function_data_practice.txt', 'r')
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

    angles = np.linspace(np.min(data[:, 0]), np.max(data[:, 0]), 100)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.errorbar(data[:, 0], data[:, 1], yerr=data[:, 2], fmt='o',
                label='data')
    for phase in PHASES:
        ax.plot(angles, function(angles, phase),
                label=r'$\phi$ = {:4.3f} (rad)'.format(phase))
    ax.legend(bbox_to_anchor=(1.04, 1))
    ax.grid(True, color='grey', dashes=[4, 2])
    ax.set_xlabel(r'\theta (degrees)')
    ax.set_ylabel(r'cos(\theta +\phi)')
    plt.show()
