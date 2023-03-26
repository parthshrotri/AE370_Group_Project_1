import numpy as np
from rk4 import Simulator
import sys
import os
from plotter import plot

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from dynamics.body import Body
from properties import prop

day_in_sec = 24*60*60

# Define system bodies
sun = Body(prop.mass_sun, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), False, 'sun')
# mercury = Body(prop.mass_mercury,)
# venus = Body(prop.mass_venus,)
earth = Body(prop.mass_earth, np.array([[-2.6E10, 1.32E11, 5.75E10], [-2.98E4*day_in_sec, -4.72E3*day_in_sec, -2.05E3*day_in_sec], [0, 0, 0]]), True, 'earth') #everything in SI
# mars = Body(prop.mass_mars,)
# jupiter = Body(prop.mass_jupiter, )
# saturn = Body(prop.mass_saturn, )
# uranus = Body(prop.mass_uranus, )
# neptune = Body(prop.mass_neptune,)
system_bodies = [sun, earth]
for body in system_bodies:
    body.set_system_bodies(system_bodies)
sim = Simulator()
sim.rk4_ivp([sun, earth], 0, 360, 60/(24*60*60))
# sim.rk4_ivp([sun, earth], 0, 1*day_in_sec, day_in_sec)

plot.plot_traj(earth)