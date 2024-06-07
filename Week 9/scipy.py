# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:14:31 2023

@author: theob
"""
import scipy.constants as pc
from scipy import special
import matplotlib.pyplot as plt
import numpy as np

print(pc.epsilon_0)

# print(dir(pc))

print(pc.hbar)
print(pc.neutron_mass)
print(pc.electron_volt)


print(special.hermite(1))
print(special.hermite(2)(0.5))


x_values = np.linspace(-2, 2, 50)
plt.plot(x_values, special.hermite(4)(x_values))
