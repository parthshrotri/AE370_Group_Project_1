import numpy as np

class Body():
    mass = 0
    # Position, velocity, acceleration of the body
    # These values are represented in Heliocentric cartesian coordinates
    state = np.zeros((3, 3)) 
    
    def __init__(self, mass, state):
        self.mass = mass
        self.state = state