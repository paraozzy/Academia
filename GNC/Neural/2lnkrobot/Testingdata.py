import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Constants for plotting
h, l1, l2 = 1, 1.6, 1.6

# Testing data for Letter X (consolidated into one plot)
x_vals = np.linspace(1, 2, 11)
y_vals_line1 = x_vals - 1
y_vals_line2 = 2 - x_vals

# Testing data for First Ellipse (Points)
theta_ellipse = np.arange(0, 360, 10)
x_ellipse = 1.5 + 0.4 * np.cos(np.radians(theta_ellipse))
y_ellipse = 0.5 + 0.2 * np.sin(np.radians(theta_ellipse))

# Testing data for Second Ellipse (Points)
theta_ellipse_2 = np.arange(0, 360, 10)
x_ellipse_2 = 1.5 + 0.5 * np.cos(np.radians(theta_ellipse_2))
y_ellipse_2 = 0.5 + 0.8 * np.sin(np.radians(theta_ellipse_2))


# Assuming theta_1 and theta_2 are not used for testing (dummy values)
theta_1_dummy = 0
theta_2_dummy = 0

# Consolidate all testing data
testing_data = []

# Letter X
for x, y in zip(np.concatenate([x_vals, x_vals]), np.concatenate([y_vals_line1, y_vals_line2])):
    testing_data.append([theta_1_dummy, theta_2_dummy, x, y])

# First Ellipse
for x, y in zip(x_ellipse, y_ellipse):
    testing_data.append([theta_1_dummy, theta_2_dummy, x, y])

# Second Ellipse
for x, y in zip(x_ellipse_2, y_ellipse_2):
    testing_data.append([theta_1_dummy, theta_2_dummy, x, y])

# Create DataFrame
testing_df = pd.DataFrame(testing_data, columns=['theta_1', 'theta_2', 'x_2', 'y_2'])

# Save to CSV
testing_df.to_csv('/Users/kka/Documents/GitHub/Academia/GNC/Neural/2lnkrobot/testing_data.csv', index=False)

# Plotting Letter X with both lines
plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals_line1, 'rx', label='Line 1: y=x-1')
plt.plot(x_vals, y_vals_line2, 'gx', label='Line 2: y=2-x')
plt.title('Letter X Testing Data')
plt.xlabel('x_2')
plt.ylabel('y_2')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()

# Plotting First Ellipse
plt.figure(figsize=(6, 6))
plt.scatter(x_ellipse, y_ellipse, color='blue', label='First Ellipse')
plt.title('First Ellipse Testing Data')
plt.xlabel('x_2')
plt.ylabel('y_2')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()

# Plotting Second Ellipse
plt.figure(figsize=(6, 6))
plt.scatter(x_ellipse_2, y_ellipse_2, color='magenta', label='Second Ellipse')
plt.title('Second Ellipse Testing Data')
plt.xlabel('x_2')
plt.ylabel('y_2')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()

# Combined plot of all three scenarios
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals_line1, 'rx', label='Letter X Line 1')
plt.plot(x_vals, y_vals_line2, 'gx', label='Letter X Line 2')
plt.scatter(x_ellipse, y_ellipse, color='blue', label='First Ellipse')
plt.scatter(x_ellipse_2, y_ellipse_2, color='magenta', label='Second Ellipse')
plt.title('Combined Testing Data')
plt.xlabel('x_2')
plt.ylabel('y_2')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()