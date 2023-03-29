import numpy as np
from rk4 import Simulator
import sys
import os
import time

sys.path.insert(0, os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')))
from plotter import plot
from dynamics.body import Body
from properties import prop

def two_body_problem(days = 365, dt = 60, plt = False):

    seconds_per_day = 24*60*60
    earth_pos = prop.earth_initial_position
    earth_vel = prop.earth_initial_velocity*seconds_per_day

    # Define system bodies
    sun = Body(prop.mass_sun, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), False, 'sun')
    earth = Body(prop.mass_earth, np.array([earth_pos, earth_vel, [0, 0, 0]]), True, 'earth') #everything in SI

    system_bodies = [sun, earth]
    for body in system_bodies:
        body.set_system_bodies(system_bodies)

    sim = Simulator()
    t_start = time.time()
    sim.rk4_ivp(system_bodies, 0, days, dt/(seconds_per_day), '../output/two_body_test/')
    t_end = time.time() - t_start
    print(f'Run at dt = {dt:.2f} completed in {t_end:.2f}sec')

    if plt == True:
        plot.plot_traj([body.name for body in system_bodies if body.name != 'sun'], 'two_body_test', days)
    
    return t_end

if __name__ == '__main__':
    two_body_problem(plt=False)