import numpy as np
from rk4 import Simulator
import sys
import os
from plotter import plot

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from dynamics.body import Body
from properties import prop

seconds_per_day = 24*60*60
days = 360
dt = 200

# Define system bodies
sun = Body(prop.mass_sun, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), False, 'sun')
mercury = Body(prop.mass_mercury, np.array([prop.mercury_initial_position, prop.mercury_initial_velocity*seconds_per_day, [0, 0, 0]]), False, 'mercury')
venus = Body(prop.mass_venus, np.array([prop.venus_initial_position, prop.venus_initial_velocity*seconds_per_day, [0, 0, 0]]), False, 'venus')
earth = Body(prop.mass_earth, np.array([prop.earth_initial_position, prop.earth_initial_velocity*seconds_per_day, [0, 0, 0]]), True, 'earth') #everything in SI
mars = Body(prop.mass_mars, np.array([prop.mars_initial_position, prop.mars_initial_velocity*seconds_per_day, [0, 0, 0]]), False, 'mars')
jupiter = Body(prop.mass_jupiter, np.array([prop.jupiter_initial_position, prop.jupiter_initial_velocity*seconds_per_day, [0, 0, 0]]), True, 'jupiter')
saturn = Body(prop.mass_saturn, np.array([prop.saturn_initial_position, prop.saturn_initial_velocity*seconds_per_day, [0, 0, 0]]), False, 'saturn')
uranus = Body(prop.mass_uranus, np.array([prop.uranus_initial_position, prop.uranus_initial_velocity*seconds_per_day, [0, 0, 0]]), False, 'uranus')
neptune = Body(prop.mass_neptune, np.array([prop.neptune_initial_position, prop.neptune_initial_velocity*seconds_per_day, [0, 0, 0]]), False, 'neptune')
# jupiter_l4 = Body(prop.mass_L4, np.array([prop.L4_initial_position, prop.L4_initial_velocity*seconds_per_day, [0,0,0]]), True, 'jupiter_l4')
# jupiter_l5 = Body(prop.mass_L5, np.array([prop.L5_initial_position, prop.L5_initial_velocity*seconds_per_day, [0,0,0]]), True, 'jupiter_l5')

system_bodies = [sun, earth, mercury, venus, mars, jupiter, saturn, uranus, neptune]

# Asteroid generation
num_asteroids = 5
# average_orbit_distance_jupiter = 778E9 # distance in m from sun
# average_orbit_distance_saturn = 1400E9 # Distance from sun in m
# asteroid_pos_distribution = 0.1
# asteroid_pos_min = 0.01
# asteroid_nominal_speed = 18000 # Nominal speed in m/s
# asteroid_speed_distribution = 0.2
# phi_range = 70
# asteroid_velocity_xy_distribution = 0.5 # Velocity direction modifier range for x and y
# asteroid_velocity_z_distribution = 0.25 # Direction modifier range for z
# asteroid_average_mass = 4.6E17 # Mass of Chicxulub asteroid 
# asteroid_mass_distribution = 1 # Asteroid mass distribution range

asteroid_masses = np.array(np.load(os.path.join(os.path.dirname(__file__), '..', 'data','asteroids', 'asteroid_masses.npy')))
asteroids_init_pos = np.array(np.load(os.path.join(os.path.dirname(__file__), '..', 'data','asteroids', 'asteroids_init_pos.npy')))
asteroids_init_vel = np.array(np.load(os.path.join(os.path.dirname(__file__), '..', 'data','asteroids', 'asteroids_init_vel.npy')))

for i in range(num_asteroids):
    # distance_from_jupiter = (asteroid_pos_distribution*np.random.random() + asteroid_pos_min)\
    #     *abs(average_orbit_distance_jupiter - average_orbit_distance_saturn) #Set position of asteroid in between jupiter and saturn orbit
    # # initial_radius = average_orbit_distance_jupiter + distance_from_jupiter
    # theta = 2*np.pi*np.random.random() # Generate some random theta between -45 and 45 degrees relative to jupiter
    # phi = np.pi/2 - (np.radians(phi_range) * (np.random.random() - 0.5)) # Generate some random phi between -10 and 10 degrees relative to jupiter
    # asteroid_initial_position = distance_from_jupiter * np.array([np.sin(phi)*np.cos(theta), np.sin(phi)*np.sin(theta), np.cos(phi)]) + prop.jupiter_initial_position
    
    
    # asteroid_initial_speed = asteroid_nominal_speed * (1 + asteroid_speed_distribution*(np.random.random() - 0.5))
    # x_modifier = 1 + (asteroid_velocity_xy_distribution * (np.random.random() - 0.5))
    # y_modifier = 1 + (asteroid_velocity_xy_distribution * (np.random.random() - 0.5))
    # z_modifier = 1 + (asteroid_velocity_z_distribution * (np.random.random() - 0.5))
    # mods = np.array([x_modifier, y_modifier, z_modifier])
    # asteroid_initial_velocity = -asteroid_initial_speed * (asteroid_initial_position * mods)/np.linalg.norm(asteroid_initial_position * mods)
    
    # asteroid_mass = asteroid_average_mass * (1+(asteroid_mass_distribution*(np.random.random() - 0.5)))
    # asteroid = Body(asteroid_mass, np.array([asteroid_initial_position, asteroid_initial_velocity*seconds_per_day, [0,0,0]]), True, 'asteroid_' + str(i))
    asteroid = Body(asteroid_masses[i], np.array([asteroids_init_pos[i], asteroids_init_vel[i]*seconds_per_day, [0,0,0]]), True, 'asteroid_' + str(i))
    system_bodies.append(asteroid)


for body in system_bodies:
    body.set_system_bodies(system_bodies)
sim = Simulator()
sim.rk4_ivp(system_bodies, 0, days, dt/seconds_per_day)
# sim.rk4_ivp([sun, earth], 0, 1*day_in_sec, day_in_sec)
# plot.plot_traj([body.name for body in system_bodies if body.name != 'sun'])