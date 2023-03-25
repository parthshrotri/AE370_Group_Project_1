from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import os

def plot(body: object):
    
    planet_list = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
    
    appx_trajectory = np.load(os.path.join(os.path.dirname(__file__, '../output/'), body.name + '_trajectory.npy'))
    x = appx_trajectory[:,0]
    y = appx_trajectory[:,1]
    z = appx_trajectory[:,2]

    fig = plt.figure(figsize=(8, 10), tight_layout=True)
    ax = plt.axes(projection = '3d')
    if body.name in planet_list:
        true_trajectory = np.load(os.path.join(os.path.dirname(__file__, '../data/'), body.name + '_trajectory.npy'))
        x_true = true_trajectory[:,0]
        y_true = true_trajectory[:,1]
        z_true = true_trajectory[:,2]
        ax.plot3D(x_true, y_true, z_true,'k.',label='True Trajectory')
    ax.plot3D(x,y,z,'r.',label='Approximated Trajectory')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    ax.set_title('Trajectory')
    ax.legend()
