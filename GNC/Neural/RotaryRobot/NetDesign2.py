import numpy as np
import pandas as pd

# Define the simulation function based on the provided equations
def simulate_robot(torque_values, time_steps):
    data = []
    for T in torque_values:
        for t in time_steps:
            theta_t = (T * t**2) / (2 * 1.75)
            omega_t = (T * t) / 1.75
            # Assuming X_1(t+1) and X_2(t+1) need to be calculated similarly or placeholders for now
            # Update theta and omega for t+1 using provided equations directly for simplicity
            t_next = t + 0.1
            theta_t1 = (T * t_next**2) / (2 * 1.75)
            omega_t1 = (T * t_next) / 1.75
            # Append the inputs (T, theta_t, omega_t) and outputs (X_1, X_2, theta_t1, omega_t1)
            # X_1, X_2 are placeholders, assuming a direct relation or additional details needed
            data.append([T, theta_t, omega_t, np.nan, np.nan, theta_t1, omega_t1])
    return np.array(data)

# Time steps for simulation
time_steps = np.arange(0, 1.2, 0.1)  # From 0 to 1.1 inclusive, with a step of 0.1

# Torques for training and testing
training_torques = [1, 2, 3, 4]
testing_torques = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]

# Simulating training and testing data
training_data = simulate_robot(training_torques, time_steps)
testing_data = simulate_robot(testing_torques, time_steps)

# Convert the arrays to DataFrames for saving to text files with headers
training_df = pd.DataFrame(training_data, columns=['T', 'theta(t)', 'omega(t)', 'X_1(t+1)', 'X_2(t+1)', 'theta(t+1)', 'omega(t+1)'])
testing_df = pd.DataFrame(testing_data, columns=['T', 'theta(t)', 'omega(t)', 'X_1(t+1)', 'X_2(t+1)', 'theta(t+1)', 'omega(t+1)'])

# Paths for the output files
training_file_path = '/Users/kka/Documents/GitHub/Academia-1/robot_training_data.txt'
testing_file_path = '/Users/kka/Documents/GitHub/Academia-1/robot_testing_data.txt'

# Save to text files
training_df.to_csv(training_file_path, sep='\t', index=False, float_format='%.4f')
testing_df.to_csv(testing_file_path, sep='\t', index=False, float_format='%.4f')

training_file_path, testing_file_path
