import numpy as np
import dynamics.forces as forces
from dynamics.body import Body

def rk4_v_step(object:Body, force:np.ndarray, t_step:float) -> tuple(np.ndarray, np.ndarray):
    ''' Perform a single step of the RK4 algorithm for the velocity of an object
    
    Args:
        object (Body): The object to be updated
        force (np.ndarray): The net force vector on the object
        t_step (float): The time step to be used
    
    Returns:
        velocity (np.ndarray): The updated velocity of the object
    '''
    a = force / object.mass
    k1 = a
    k2 = a + 0.5 * t_step * k1
    k3 = a + 0.5 * t_step * k2
    k4 = a + t_step * k3
    
    v = object.get_velocity() + (t_step / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    
    return v, a

def rk4_p_step(object:Body, force:np.ndarray, t_step:float) -> None:
    ''' Perform a single step of the RK4 algorithm for the position of an object
        Calculates both the updated position and updated velocity of the object
        Updates the state of the body object
    Args:
        object (Body): The object to be updated
        force (np.ndarray): The net force vector on the object
        t_step (float): The time step to be used
    
    Returns:
        None
    '''
    v, a = rk4_v_step(object, force, t_step)

    k1 = v
    k2 = v + 0.5 * t_step * k1
    k3 = v + 0.5 * t_step * k2
    k4 = v + t_step * k3
    
    p = object.get_position() + (t_step / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    object.set_acceleration(a)
    object.set_velocity(v)
    object.set_position(p)
    
def rk4_ivp(objects:list, t_start:float, t_end:float, t_step:float) -> None:
    ''' Perform the RK4 algorithm for a system of objects
    
    Args:
        objects (list): A list of Body objects
        t_start (float): The start time of the simulation
        t_end (float): The end time of the simulation
        t_step (float): The time step to be used
        
    Returns:
        None
    '''
    t = t_start
    while t < t_end:
        
        # Store the net force vector on each object
        force_list = []
        for i in range(objects):
            force_list.append(objects[i].get_forces())

        for i in range(objects):
            rk4_p_step(objects[i], force_list[i], t_step)
        t += t_step
        