# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:54:29 2023

@author: theob
"""

import numpy as np

import matplotlib.pyplot as plt


# Load data from the first CSV file
data1 = np.genfromtxt('z_boson_data_1.csv', delimiter=',', skip_header=1,
                      dtype=float, missing_values='fail', filling_values=np.nan)

# Load data from the second CSV file
data2 = np.genfromtxt('z_boson_data_2.csv', delimiter=',', skip_header=1,
                      dtype=float, missing_values='fail', filling_values=np.nan)

# Stack the data vertically
combined_data = np.vstack((data1, data2))

# Save the combined data to a new CSV file
np.savetxt('combined_data_vertical.csv', combined_data, fmt='%.4f',
           delimiter=',', header='Centre-of-mass energy (GeV),Cross section (nb),Uncertainty (nb)', comments='')

print("Combined data has been saved to combined_data_vertical.csv")


# Load combined data with np.nan values
combined_data = np.genfromtxt(
    'combined_data_vertical.csv', delimiter=',', skip_header=1)

# Extract columns
energy = combined_data[:, 0]
cross_section = combined_data[:, 1]
uncertainty = combined_data[:, 2]

# Identify indices of NaN values in any column
nan_indices = np.any(np.isnan(combined_data), axis=1)

# Remove rows with NaN values from the data
filtered_data = combined_data[~nan_indices]

# Extract columns from the filtered data
filtered_energy = filtered_data[:, 0]
filtered_cross_section = filtered_data[:, 1]
filtered_uncertainty = filtered_data[:, 2]


# Calculate the mean and standard deviation of cross-section
mean_cross_section = np.mean(filtered_cross_section)
std_cross_section = np.std(filtered_cross_section)

# Define a threshold for outliers (e.g., 3 times the standard deviation)
threshold = 3 * std_cross_section

# Identify indices of outliers
outlier_indices = np.where(
    np.abs(filtered_cross_section - mean_cross_section) > threshold)[0]

# Remove outliers from the data
filtered_energy2 = np.delete(filtered_energy, outlier_indices)
filtered_cross_section2 = np.delete(filtered_cross_section, outlier_indices)
filtered_uncertainty2 = np.delete(filtered_uncertainty, outlier_indices)

# Plot the data without outliers
plt.errorbar(filtered_energy2, filtered_cross_section2,
             yerr=filtered_uncertainty2, fmt='o', label='Data without outliers')

# Add labels and title
plt.xlabel('Centre-of-mass energy (GeV)')
plt.ylabel('Cross section (nb)')
plt.title('Data Plot without Outliers')

# Show the legend
plt.legend()

# Show the plot
plt.show()
