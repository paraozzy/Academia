import numpy as np
import pandas as pd  # Import pandas

# Constants
l = 2  # length of the arm
J = 1.75  # moment of inertia
time_steps = np.arange(0, 1.2, 0.1)  # time steps from 0 to 1.1 inclusive
T_train = [1, 2, 3, 4]  # training torque values
T_test = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]  # testing torque values

def generate_dataset(T_values):
    dataset = []
    for T in T_values:
        theta = 0
        omega = 0
        for t in time_steps:
            X_1 = l * np.cos(theta)
            X_2 = l * np.sin(theta)
            theta_next = (T * t**2) / (2 * J)
            omega_next =(T * t) / J
            dataset.append([T, theta, omega, X_1, X_2, theta_next, omega_next])
            # Update for next step
            theta, omega = theta_next, omega_next
    return np.array(dataset)

# Generate training and testing datasets
train_dataset = generate_dataset(T_train)
test_dataset = generate_dataset(T_test)

# Convert numpy arrays to pandas DataFrames with appropriate column names
columns = ['T', 'theta(t)', 'omega(t)', 'X_1(t+1)', 'X_2(t+1)', 'theta(t+1)', 'omega(t+1)']
train_df = pd.DataFrame(train_dataset, columns=columns)
test_df = pd.DataFrame(test_dataset, columns=columns)

# Specify file names
train_file_name = 'training_data.csv'
test_file_name = 'testing_data.csv'

# Save to CSV files
train_df.to_csv(train_file_name, index=False)
test_df.to_csv(test_file_name, index=False)

print(f"Training data saved to {train_file_name}")
print(f"Testing data saved to {test_file_name}")
