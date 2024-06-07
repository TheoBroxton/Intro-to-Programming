# -*- coding: utf-8 -*-
"""
PHYS20161 Week 3 PRACTICE quiz - Tribonacci series
Lloyd Cawthorne 28/05/19

This code finds the largest element of the tribonacci series less than or equal
to the input given.

The tribonacci series ( http://mathworld.wolfram.com/TribonacciNumber.html ) is
a generalisation of the fiboncci sequence, however, there are three starting
parameters and three numbers are summed for each additional number.

WARNING: It might run but give incorrect results!
(Hint: check by hand where reasonable)

"""


def largest_tribonacci_element(end_input):
    """
    Returns the largest element (int) of the Tribonacci sequence less than
    or equal to the input given.
    Args:
        end_input (int)
    """
    # Initial parameters

    n_0 = n_1 = 0
    n_2 = 1

    n = 1

    # Edge case

    if end_input == 0:

        n_2 = 0

    # Standard format of series
    else:

        while n <= end_input:

            # Continuosly update parameters accordingly
            n = n_0 + n_1 + n_2
            n_0 = n_1
            n_1 = n_2
            n_2 = n

    print("The largest element of the tribonacci series less than or equal to "
          "{0:d} is {1:d}.".format(end_input, n_1))

    return n_2


end_string = input("What is the upper limit for this series? ")

end = int(end_string)

largest_tribonacci_element(end)
