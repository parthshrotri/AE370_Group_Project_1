from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import os

def plot(bodies: list, days=20*365):
    
    planet_list = ['mercury', 'venus','earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'moon']
    
    
    # print(x)
    #print(appx_trajectory)

    fig = plt.figure(figsize=(8, 10), tight_layout=True)
    ax = fig.add_subplot( 111 , projection = '3d')
    # if body in planet_list:
    #     true_trajectory = np.load(os.path.join(os.path.dirname(__file__), '../data/npy_files', body.name + '_trajectory.npy'))
    #     x_true = true_trajectory[:,0]
    #     y_true = true_trajectory[:,1]
    #     z_true = true_trajectory[:,2]
    #     ax.plot3D(x_true*1000, y_true*1000, z_true*1000,'k.',label='True Trajectory')
    for body in bodies:
        if body in planet_list:
            true_trajectory = np.load(os.path.join(os.path.dirname(__file__), '../data/npy_files', body + '_trajectory.npy'))
            x_true = true_trajectory[:days,0]
            y_true = true_trajectory[:days,1]
            z_true = true_trajectory[:days,2]
            ax.plot3D(x_true*1000, y_true*1000, z_true*1000,'-',label=body + ' True Trajectory')
        appx_trajectory = np.load(os.path.join(os.path.dirname(__file__), '..','output', body + '_trajectory.npy'))
        x = appx_trajectory[:,0]
        y = appx_trajectory[:,1]
        z = appx_trajectory[:,2]
        ax.plot3D(x,y,z,'-',label= body + ' Approximated Trajectory')
    ax.plot3D(0, 0, 0, '.', label='Sun', color='blue')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    # ax.set_title('Trajectory of )
    ax.legend()
    plt.show()
if __name__ == '__main__':
    plot(['earth', 'moon'])
# plot(['earth', 'jwst'])