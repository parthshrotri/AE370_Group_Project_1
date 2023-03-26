import numpy as np
from rk4 import Simulator
import sys
import os
import time
from plotter import plot

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from dynamics.body import Body
from properties import prop

seconds_per_day = 24*60*60
days = 5*365
earth_pos = np.array([-2.600745330322259E+10,  1.326237828764555E+11,  5.752511716959091E+10])
earth_vel = np.array([-2.983800155786667E+04, -4.724379075830139E+03, -2.047849455589723E+03,])*seconds_per_day
moon_pos = np.array([-2.637093499608123E+10, 1.327648230502377E+11, 5.761337388984415E+10])
moon_vel = np.array([-3.024279048864922E+04, -5.494701852227165E+03, -2.445635834561632E+03])*seconds_per_day

# Define system bodies
sun = Body(prop.mass_sun, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), False, 'sun')
earth = Body(prop.mass_earth, np.array([earth_pos, earth_vel, [0, 0, 0]]), True, 'earth') #everything in SI
moon = Body(prop.mass_moon, np.array([moon_pos, moon_vel, [0, 0, 0]]), True, 'moon')

system_bodies = [sun, earth, moon]
for body in system_bodies:
    body.set_system_bodies(system_bodies)

sim = Simulator()
t_start = time.time()
sim.rk4_ivp(system_bodies, 0, days, 60/(seconds_per_day))
t_end = time.time() - t_start
print(f"Time: {t_end:.2f}")

plot.plot([body.name for body in system_bodies if body.name != 'sun'], days)