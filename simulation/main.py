import numpy as np
from rk4 import Simulator
import sys
import os
from plotter import plot

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from dynamics.body import Body
from properties import prop
# Define system bodies
sun = Body(prop.mass_sun, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], False, 'Sun')
# mercury = Body(prop.mass_mercury,)
# venus = Body(prop.mass_venus,)
earth = Body(prop.mass_earth, [[150E9, 0, 0], [0, 29722.22, 0], [-3.5172E22, 0, 0]], True, 'Earth')         #everything in SI
# mars = Body(prop.mass_mars,)
# jupiter = Body(prop.mass_jupiter, )
# saturn = Body(prop.mass_saturn, )
# uranus = Body(prop.mass_uranus, )
# neptune = Body(prop.mass_neptune,)

sim = Simulator()
day_in_sec = 24*60*60
sim.rk4_ivp([sun, earth], 0, 400 * day_in_sec, day_in_sec)
print(earth.get_position())

plot.plot()
