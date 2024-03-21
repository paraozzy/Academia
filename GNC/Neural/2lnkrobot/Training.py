import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
h = 1.0
l1 = l2 = 1.6

# Function to calculate x_2 and y_2
def calculate_positions(theta_1, theta_2):
    theta_1_rad = np.radians(theta_1)
    theta_2_rad = np.radians(theta_2)
    x_2 = l1 * np.cos(theta_1_rad - np.pi/2) + l2 * np.sin(theta_2_rad + theta_1_rad - np.pi)
    y_2 = h + l1 * np.sin(theta_1_rad - np.pi/2) - l2 * np.cos(theta_2_rad + theta_1_rad - np.pi)
    return x_2, y_2

# Generate a range of theta_1 values (for example purposes, adjust as needed)
theta_1_range = np.linspace(-180, 180, 360)

# Now, we explicitly define theta_2_range to respect the constraint [0, 180]
theta_2_range = np.linspace(0, 180, 180)

# Prepare the dataset with the theta_2 constraint
training_data = []

for theta_1 in theta_1_range:
    for theta_2 in theta_2_range:
        x_2, y_2 = calculate_positions(theta_1, theta_2)
        training_data.append([theta_1, theta_2, x_2, y_2])

training_df = pd.DataFrame(training_data, columns=['theta_1', 'theta_2', 'x_2', 'y_2'])

# Placeholder arrays for demonstration purposes; replace these with your actual data

# Plot y_2 vs. x_2 from the training dataframe
plt.figure(figsize=(8, 6))
plt.scatter(training_df['x_2'], training_df['y_2'], color='blue', label='Training Data Points')
plt.title('Training Data: Target y_2 vs. x_2')
plt.xlabel('x_2')
plt.ylabel('y_2')
plt.grid(True)
plt.legend()
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.show()

training_df.to_csv('/Users/kka/Documents/GitHub/Academia/GNC/Neural/2lnkrobot/training_data.csv', index=False)