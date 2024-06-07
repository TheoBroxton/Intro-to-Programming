# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 15:48:26 2023

@author: theob
"""


def plot_combined_data(combined_data, save_path='scatter_plot.png'):
    """
    Plot the combined data with uncertainties and save the figure as a PNG file.

    Parameters
    ----------
    combined_data : numpy array
        Combined data to be plotted.
    save_path : str, optional
        File path to save the figure as a PNG file. Defaults to 'scatter_plot.png'.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    x_values = combined_data[:, 0]
    y_values = combined_data[:, 1]
    uncertainties = combined_data[:, 2]

    ax.errorbar(x_values, y_values, yerr=uncertainties,
                fmt='o', label='Data with Uncertainties')
    ax.set_title('Scatter Plot with Uncertainties')
    ax.set_xlabel('Centre-of-mass energy (GeV)')
    ax.set_ylabel('Cross section (nb)')
    ax.legend()

    plt.savefig(save_path, bbox_inches='tight', dpi=600)
    plt.show()
    plt.close()
