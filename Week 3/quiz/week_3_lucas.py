# -*- coding: utf-8 -*-
"""
PHYS20161 Week 3 quiz - Lucas series
Lloyd Cawthorne 23/05/19

This code finds the largest element of the Lucas series lower than or equal to
the input given.

The Lucas series is similar to the Fibonacci, but has different starting
parameters.

Correct 5 bugs to get it working. Then, use the inputs requested in Blackboard.

WARING: the code might run but give incorrect results!!

"""


def largest_lucas_element(end_input):
    """
    Returns the largest element (int) of the Lucas sequence less than or
    equal to the input given.
    Args:
        end_input (int)
    """
    # Initial parameters
    n_0 = 2
    n_1 = 1
    n = 3

    # Correct for first two entries
    if end_input = 0:
        print("There are no elements of the Lucas sequence equal to zero.")
    elif end_input == 2:
        print('The largest element of the Lucas series less than or equal to 2'
              'is 2.')
    elif end_input == 1:
        print('The largest element of the Lucas series less than or equal to 1'
              ' is 1.')

    # Standard format of series
    else:
        while n < end_input:

            # Continuosly update parameters accordingly
            n_0 = n_1
            n_1 = n
            n = n_0 + n_1

        print('The largest element of the Lucas series less than or equal to '
              '{0:d} is {1:d}.'.format(end_input, n_0))
    return n_1


end_string = ("What is the upper limit for this series? ")

end int(end_string)

largest_lucas_element(end)
