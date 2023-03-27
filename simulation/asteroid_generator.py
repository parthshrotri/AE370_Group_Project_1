import numpy as np

from rk4 import Simulator
import sys
import os
from plotter import plot

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from dynamics.body import Body
from properties import prop

num_asteroids = 5
average_orbit_distance_jupiter = 778E9 # distance in m from sun
average_orbit_distance_saturn = 1400E9 # Distance from sun in m
asteroid_pos_distribution = 0.2
asteroid_pos_min = 0.125
asteroid_nominal_speed = 18000 # Nominal speed in m/s
asteroid_speed_distribution = 0.2
phi_range = 70
asteroid_velocity_xy_distribution = 0.5 # Velocity direction modifier range for x and y
asteroid_velocity_z_distribution = 0.25 # Direction modifier range for z
asteroid_average_mass = 4.6E17 # Mass of Chicxulub asteroid 
asteroid_mass_distribution = 1 # Asteroid mass distribution range

asteroid_masses = np.array([])
asteroids_init_pos = np.array([])
asteroids_init_vel = np.array([])
for i in range(num_asteroids):
    distance_from_jupiter = (asteroid_pos_distribution*np.random.random() + asteroid_pos_min)\
        *abs(average_orbit_distance_jupiter - average_orbit_distance_saturn) #Set position of asteroid in between jupiter and saturn orbit
    # initial_radius = average_orbit_distance_jupiter + distance_from_jupiter
    theta = np.radians(30)+np.pi/2*np.random.random() # Generate some random theta between 0 and 90 degrees relative to jupiter
    phi = np.pi/2 - (np.radians(phi_range) * (np.random.random() - 0.5)) # Generate some random phi between -10 and 10 degrees relative to jupiter
    asteroid_initial_position = distance_from_jupiter * np.array([np.sin(phi)*np.cos(theta), np.sin(phi)*np.sin(theta), np.cos(phi)]) + prop.jupiter_initial_position
    
    
    asteroid_initial_speed = asteroid_nominal_speed * (1 + asteroid_speed_distribution*(np.random.random() - 0.5))
    x_modifier = 1 + (asteroid_velocity_xy_distribution * (np.random.random() - 0.5))
    y_modifier = 1 + (asteroid_velocity_xy_distribution * (np.random.random() - 0.5))
    z_modifier = 1 + (asteroid_velocity_z_distribution * (np.random.random() - 0.5))
    mods = np.array([x_modifier, y_modifier, z_modifier])
    asteroid_initial_velocity = -asteroid_initial_speed * (asteroid_initial_position * mods)/np.linalg.norm(asteroid_initial_position * mods)
    
    asteroid_mass = asteroid_average_mass * (1+(asteroid_mass_distribution*(np.random.random() - 0.5)))
    asteroid_masses = np.append(asteroid_masses, asteroid_mass)
    asteroids_init_pos = np.append(asteroids_init_pos, asteroid_initial_position)
    asteroids_init_vel = np.append(asteroids_init_vel, asteroid_initial_velocity)

asteroids_init_pos = asteroids_init_pos.reshape((num_asteroids, 3))
asteroids_init_vel = asteroids_init_vel.reshape((num_asteroids, 3))

if os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'data', 'asteroids')):
    for file in os.listdir(os.path.join(os.path.dirname(__file__), '..', 'data', 'asteroids')):
        os.remove(os.path.join(os.path.dirname(__file__), '..', 'data', 'asteroids', file))
np.save(os.path.join(os.path.dirname(__file__), '..', 'data', 'asteroids', 'asteroid_masses.npy'), asteroid_masses)
np.save(os.path.join(os.path.dirname(__file__), '..', 'data', 'asteroids', 'asteroids_init_pos.npy'), asteroids_init_pos)
np.save(os.path.join(os.path.dirname(__file__), '..', 'data', 'asteroids', 'asteroids_init_vel.npy'), asteroids_init_vel)