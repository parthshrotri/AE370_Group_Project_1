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
days = 30
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

asteroid_masses = np.array(np.load(os.path.join(os.path.dirname(__file__), '..', 'data','asteroids', 'asteroid_masses.npy')))
asteroids_init_pos = np.array(np.load(os.path.join(os.path.dirname(__file__), '..', 'data','asteroids', 'asteroids_init_pos.npy')))
asteroids_init_vel = np.array(np.load(os.path.join(os.path.dirname(__file__), '..', 'data','asteroids', 'asteroids_init_vel.npy')))

for i in range(num_asteroids):
    asteroid = Body(asteroid_masses[i], np.array([asteroids_init_pos[i], asteroids_init_vel[i]*seconds_per_day, [0,0,0]]), True, 'asteroid_' + str(i))
    system_bodies.append(asteroid)


for body in system_bodies:
    body.set_system_bodies(system_bodies)
sim = Simulator()
sim.rk4_ivp(system_bodies, 0, days, dt/seconds_per_day, save_folder='../output/without_jupiter/')
# sim.rk4_ivp([sun, earth], 0, 1*day_in_sec, day_in_sec)
# plot.plot_traj([body.name for body in system_bodies if body.name != 'sun'])