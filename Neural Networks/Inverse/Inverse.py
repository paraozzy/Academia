import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
h, l1, l2 = 1, 1.6, 1.6

# Corrected function to calculate x_2 and y_2 given theta_1 and theta_2
def calculate_x2_y2(theta_1, theta_2):
    x_2 = l1 * np.cos(np.radians(theta_1 - 90)) + l2 * np.sin(np.radians(theta_2 + theta_1 - 180))
    y_2 = h + l1 * np.sin(np.radians(theta_1 - 90)) - l2 * np.cos(np.radians(theta_2 + theta_1 - 180))
    return x_2, y_2

# Example: Generate testing data for Letter X and Ellipse (adjust code to generate training data as needed)

# Testing data for Letter X
x_vals = np.linspace(1, 2, 11)
y_vals_line1 = x_vals - 1
y_vals_line2 = 2 - x_vals

# Testing data for Ellipse
theta_ellipse = np.arange(0, 360, 10)
x_ellipse = 1.5 + 0.4 * np.cos(np.radians(theta_ellipse))
y_ellipse = 0.5 + 0.2 * np.sin(np.radians(theta_ellipse))

# Given values for the second ellipse
theta_ellipse_2 = np.arange(0, 360, 10)  # Degrees
x_ellipse_2 = 1.5 + 0.5 * np.cos(np.radians(theta_ellipse_2))  # x_2 formula for the second ellipse
y_ellipse_2 = 0.5 + 0.8 * np.sin(np.radians(theta_ellipse_2))  # y_2 formula for the second ellipse

# Plotting for visualization
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x_vals, y_vals_line1, 'ro', label='Line 1')
plt.plot(x_vals, y_vals_line2, 'bx', label='Line 2')
plt.title('Letter X Testing Data')
plt.xlabel('x_2')
plt.ylabel('y_2')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x_ellipse, y_ellipse, 'g-', label='Ellipse')
plt.title('Ellipse Testing Data')
plt.xlabel('x_2')
plt.ylabel('y_2')
plt.legend()
plt.grid(True)

# Plotting the second ellipse
plt.figure(figsize=(6, 6))
plt.plot(x_ellipse_2, y_ellipse_2, 'm-', label='Second Ellipse')
plt.title('Second Ellipse Testing Data')
plt.xlabel('x_2')
plt.ylabel('y_2')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.legend()
plt.grid(True)
plt.axis('equal')  # Ensuring equal scaling on both axes
plt.show()

plt.tight_layout()
plt.show()
