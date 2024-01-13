import numpy as np
import matplotlib.pyplot as plt

# Constantes gravitacionais
G = 6.67430e-20  # m^3/kg/s^2, constante gravitacional
M = 5.972e24     # kg, massa da Terra

# Função para calcular a velocidade orbital
def orbital_velocity(semi_major_axis):
    return np.sqrt(G * M / semi_major_axis)

# Função para calcular o delta v necessário para a transferência de órbita
def delta_v_to_transfer(initial_radius, final_radius):
    vi = orbital_velocity(initial_radius)
    vf = orbital_velocity(final_radius)
    delta_v = np.abs(vf - vi)
    return delta_v

# Função para calcular a anomalia verdadeira dado o tempo e o período orbital
def true_anomaly(time, orbital_period):
    n = 2 * np.pi / orbital_period
    return n * time

# Função para calcular as posições (coordenadas polares) ao longo da órbita
def orbital_positions(semi_major_axis, eccentricity, time_points):
    r = semi_major_axis * (1 - eccentricity**2) / (1 + eccentricity * np.cos(true_anomaly(time_points, 2 * np.pi)))
    theta = true_anomaly(time_points, 2 * np.pi)
    return r, theta

# Parâmetros das órbitas inicial e final
initial_radius = 7000e3  # metros
final_radius = 15000e3   # metros
transfer_duration = 5000 # segundos

# Cálculo do delta v necessário para a transferência
delta_v = delta_v_to_transfer(initial_radius, final_radius)
print(f'Delta v necessário para a transferência: {delta_v:.2f} m/s')

# Geração de pontos temporais para a simulação
time_points = np.linspace(0, transfer_duration, num=1000)

# Cálculo das posições orbitais ao longo do tempo para as duas órbitas
initial_orbit = orbital_positions(initial_radius, 0, time_points)
transfer_orbit = orbital_positions((initial_radius + final_radius) / 2, 0.5, time_points)
final_orbit = orbital_positions(final_radius, 0, time_points)

# Cálculo das velocidades para entrar e sair da órbita de transferência
vi_enter = orbital_velocity(initial_radius)
vf_enter = orbital_velocity((initial_radius + final_radius) / 2)
vi_exit = orbital_velocity((initial_radius + final_radius) / 2)
vf_exit = orbital_velocity(final_radius)

# Print das velocidades de transferência
print(f'Velocidade para entrar na órbita de transferência: {vi_enter:.2f} m/s')
print(f'Velocidade para sair da órbita de transferência: {vf_exit:.2f} m/s')

# Plotagem das órbitas com pontos
plt.figure(figsize=(10, 6))
plt.polar(initial_orbit[1], initial_orbit[0], label='Órbita Inicial', linestyle='None', marker='o', markersize=1)
plt.polar(transfer_orbit[1], transfer_orbit[0], label='Órbita de Transferência', linestyle='None', marker='o', markersize=1)
plt.polar(final_orbit[1], final_orbit[0], label='Órbita Final', linestyle='None', marker='o', markersize=1)
plt.legend()
plt.title('Transferência Orbital')
plt.show()
