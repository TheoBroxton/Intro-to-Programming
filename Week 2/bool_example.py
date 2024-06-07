# -*- coding: utf-8 -*-
"""
Example of functions

PHYS20161 Week 2

Theo Broxton 30/9/23
"""

def logic_function(bool1, bool2):
    """
    Logic function based on two booleans
    XOR logic function
    Parameters
    ----------
    bool1 : bool
    bool2 : bool

    Returns
    -------
    bool

    """
    return(bool1 or bool2) and not (bool1 and bool2)


if logic_function(True, False):
    print("This is true")
    
print("This is written outside of if condition")
