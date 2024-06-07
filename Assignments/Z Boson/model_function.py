# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 20:15:12 2023

@author: theob
"""
import numpy as np
import matplotlib.pyplot as plt

CONVERSION_FACTOR = 0.3894e6
GAMMA_EE = 83.91e-3


def model_function(energy, m_z, gamma_z, gamma_ee=GAMMA_EE):
    """
    Calculate the model prediction.

    Parameters
    ----------
    energy : numpy array
        Input values (center-of-mass energy).
    m_z : float
        Resonance mass parameter.
    gamma_z : float
        Resonance width parameter.
    gamma_ee : float, optional
        Electron coupling parameter (default is GAMMA_EE).

    Returns
    -------
    numpy array
        Model predictions.
    """
    sigma = CONVERSION_FACTOR * (12 * np.pi / m_z**2) * (energy**2 /
                                                         ((energy**2 - m_z**2)**2 + m_z**2 * gamma_z**2)) * gamma_ee**2
    return sigma


fig, ax = plt.subplots(figsize=(10, 6))


x_range = np.linspace(85, 95, 1000)
model_predictions = model_function(x_range, 90, 3)
ax.plot(x_range, model_predictions, label='Fitted Curve', color='red')
ax.legend()
ax.set_xlabel('Centre-of-mass energy (GeV)')
ax.set_ylabel('Cross section (nb)')
plt.savefig('model_function.png', dpi=600)
plt.show()
