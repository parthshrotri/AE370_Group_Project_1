import numpy as np
from forces import Forces

class Body():
    mass = 0
    # Position, velocity, acceleration of the body
    # These values are represented in Heliocentric cartesian coordinates
    state = np.zeros((3, 3)) 
    ''' State matrix is a 3x3 matrix with the following structure:
        [[x, y, z], 
        [vx, vy, vz], 
        [ax, ay, az]]
    '''
    
    def __init__(self, mass, state, system_bodies):
        self.mass = mass
        self.state = state
        self.force = Forces(self.mass, system_bodies=system_bodies)
        
    def get_position(self):
        return self.state[0]
    
    def get_velocity(self):
        return self.state[1]
    
    def get_acceleration(self):
        return self.state[2]
    
    def set_position(self, position):
        self.state[0] = position
    
    def set_velocity(self, velocity):
        self.state[1] = velocity
        
    def set_acceleration(self, acceleration):
        self.state[2] = acceleration