import numpy as np

class Forces:
    G = 6.6743e-11 # Gravitational constant
    body_mass = 0 # Mass of the body
    system_bodies = [] # List of bodies (Body object) in the system not including the current one
    
    def __init__(self, body_mass, system_bodies):
        self.body_mass = body_mass
        self.system_bodies = system_bodies
    
    def get_forces(self) -> np.ndarray:
        '''Returns the net gravitational force on the body
        
        Returns:
            net_force (np.array): Total gravitational force on the body
        '''
        net_force = np.zeros((3, 3))
        for body in self.system_bodies:
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
    
    def _spherical_to_cartesian(self, r, theta, phi):
        '''Converts spherical coordinates to cartesian coordinates'''
        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)
        return np.array([x, y, z])
    
    def _cartesian_to_spherical(self, x, y, z):
        '''Converts cartesian coordinates to spherical coordinates'''
        r = np.sqrt(x**2 + y**2 + z**2)
        theta = np.arctan(y / x)
        phi = np.arccos(z / r)
        return np.array([r, theta, phi])
    