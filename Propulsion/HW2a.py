import numpy as np

M_a = 2.5
# Constants
gamma_a = 1.4  
gamma_d = 1.38 
gamma_B = 1.35 
gamma_n = 1.36 
R = 287  # J/(kg.K)
T04 = 2500  # K, fixed total temperature at station 4
C_d = 0.5  # Drag coefficient
fuel_mass = 200  # kg
Pr_b = 1  # Pressure ratio across the burner
eta_d = 0.98  # Diffuser efficiency
eta_n = 0.98  
QR=45000000 #J/Kg

# Altitudes and corresponding standard atmosphere values from Anderson
standard_atmosphere_values = {
    6000: {'Pa': 47217, 'Ta': 249.20, 'rho_a': 0.66011},
    10500: {'Pa': 24922, 'Ta': 220.02, 'rho_a': 0.38857},
    15000: {'Pa': 12112, 'Ta': 216.66, 'rho_a': 0.19475},
}

# Function for Speed of Sound.
def speed_of_sound(Ta, gamma, R):
    return np.sqrt(gamma * R * Ta)

# Function to calculate the parameters
def calculate_parameters(altitude, standard_atmosphere_values):
    Pa = standard_atmosphere_values[altitude]['Pa']
    Ta = standard_atmosphere_values[altitude]['Ta']
    rho_a = standard_atmosphere_values[altitude]['rho_a']
    
    # Calculate U∞ (freestream velocity)
    a = speed_of_sound(Ta, gamma_a, R)
    U_inf = M_a * a
    
    # Calculate T02 using isentropic relations
    T02 = Ta * (1 + (gamma_d - 1)/2 * M_a**2)
    
    # Calculate P0a using isentropic relations
    P0a = Pa * (1 + (gamma_d - 1)/2 * M_a**2)**(gamma_d / (gamma_d - 1))
    
    # Calculate P02
    P02 = P0a*0.78896822 # Pressure ratio is given.
    
    # Given T04 and Pr_b, calculate f (fuel-air ratio)
    cpB = 1107 # J/(kg.K)
    f = (T04 - T02)/((QR/cpB)-T04)
    P7=Pa
    P04 = Pr_b*P02
    # Calculate Ue (exit velocity)
    Ue=(((2*eta_n*gamma_n*R*T04)/(gamma_n-1))*(1-(P7/P04)**((gamma_n-1)/gamma_n)))**0.5
    
    # Specific Thrust
    specific_thrust = ((1 + f) * Ue - U_inf)
    
    # Thrust Specific Fuel consumption
    TSFC = f / specific_thrust
    
    # Area
    A = (np.pi*0.5**2)/4
    
    # Thrust
    thrust = 0.5 * rho_a * U_inf**2 * C_d * A  
    
    # mdot fuel (fuel mass flow rate)
    mdot_fuel = f * thrust / specific_thrust
    
    # Time of flight
    time_of_flight = 200 / mdot_fuel
    
    # Range
    range_km = U_inf * time_of_flight / 1000  
    return {
        'altitude': altitude,
        'Pa': Pa,
        'Ta': Ta,
        'rho_a': rho_a,
        'U_inf': U_inf,
        'T02': T02,
        'P0a': P0a,
        'P02': P02,
        'T04': T04,
        'f': f,
        'Ue': Ue,
        'Specific Thrust': specific_thrust,
        'TSFC': TSFC,
        'Thrust': thrust,
        'mdot fuel': mdot_fuel,
        'Time of flight': time_of_flight,
        'Range': range_km
    }

# Looping for the different altitudes
for altitude in standard_atmosphere_values:
    params = calculate_parameters(altitude, standard_atmosphere_values)
    for key, value in params.items():
        print(f"{key}: {value}")