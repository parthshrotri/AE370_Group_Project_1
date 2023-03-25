import numpy as np

class Body():
    G = 6.6743e-11 # Gravitational constant
    body_mass = 0 # Mass of the body
    system_bodies = [] # List of bodies (Body object) in the system not including the current one
    # Position, velocity, acceleration of the body
    # These values are represented in Heliocentric cartesian coordinates
    state = np.zeros((3, 3)) 
    ''' State matrix is a 3x3 matrix with the following structure:
        [[x, y, z], 
        [vx, vy, vz], 
        [ax, ay, az]]
    '''
    name = ''
    def __init__(self, body_mass, state, calculate_forces=True, name='Body'):
        self.body_mass = body_mass
        self.state = state
        self.calculate_forces = calculate_forces
        self.store_position = []
        self.name = name
    
    def set_system_bodies(self, bodies):
        self.system_bodies = bodies
         
    def get_forces(self) -> np.ndarray:
        '''Returns the net gravitational force on the body
        
        Returns:
            net_force (np.array): Total gravitational force on the body
        '''
        net_force = np.zeros((3, 3))
        for body in self.system_bodies:
            if body != self:
                net_force += self._get_gravitational_force(body)

        return net_force
    
    def _get_gravitational_force(self, body) -> np.ndarray:
        '''Returns the gravitational force on the body from another body
        
        Args:
            body (Body): The body that the gravitational force is being calculated from
        
        Returns:
            np.array: The gravitational force on the body from another body
        '''
        
        return (self.G * self.body_mass * body.mass / self._get_distance(body)**2) * self._get_unit_vector(body)
    
    def _get_distance(self, body):
        '''Returns the distance between the body and another body
        
        Args:
            body (Body): The body that the distance is being calculated to
        
        Returns:
            float: The distance between the body and another body
        '''
        return np.linalg.norm(body.state[0] - self.state[0])
    
    def _get_unit_vector(self, body):
        '''Returns the unit vector from the body to another body
        
        Args:
            body (Body): The body that the unit vector is being calculated to
        
        Returns:
            np.array: The unit vector from the body to another body
        '''
        
        return (body.state[0] - self.state[0]) / self._get_distance(body)
    
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