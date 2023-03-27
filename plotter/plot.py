from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import os

def plot_traj(bodies: list, file_loc: str, days=20*365, plot_true=True):
    planet_list = ['mercury', 'venus','earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'moon']
    
    fig = plt.figure(figsize=(8, 10), tight_layout=True)
    ax = fig.add_subplot( 111 , projection = '3d')
    for body in bodies:
        if body in planet_list and plot_true:
            true_trajectory = np.load(os.path.join(os.path.dirname(__file__), '../data/npy_files', body + '_trajectory.npy'))
            x_true = true_trajectory[:days+1,0]*1000
            y_true = true_trajectory[:days+1,1]*1000
            z_true = true_trajectory[:days+1,2]*1000
            ax.plot3D(x_true, y_true, z_true,'-',label=body + ' True Trajectory')
        appx_trajectory = np.load(os.path.join(os.path.dirname(__file__), '..','output', file_loc, body + '_trajectory.npy'))
        x = appx_trajectory[:,0]
        y = appx_trajectory[:,1]
        z = appx_trajectory[:,2]
        if not body.startswith('asteroid'):
            ax.plot3D(x,y,z,'-',label= body + ' Approximated Trajectory')
        else:
            ax.plot3D(x,y,z,'-')

        ufinal = np.array([x[-1],y[-1],z[-1]])
        
            
    ax.plot3D(0, 0, 0, '.', label='Sun', color='blue')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    # ax.set_title('Trajectory of )
    ax.legend()
    plt.show()

def error(bodies: list, file_loc: str, days=20*365):
    planet_list = ['mercury', 'venus','earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'moon']
    err_vals = []
    for body in bodies:
        appx_trajectory = np.load(os.path.join(os.path.dirname(__file__), '..','output', file_loc,  body + '_trajectory.npy'))
        x = appx_trajectory[:,0]
        y = appx_trajectory[:,1]
        z = appx_trajectory[:,2]
        ufinal = np.array([x[-1],y[-1],z[-1]])
        if body in planet_list:
            true_trajectory = np.load(os.path.join(os.path.dirname(__file__), '../data/npy_files', body + '_trajectory.npy'))
            x_true = true_trajectory[:days+1,0]*1000
            y_true = true_trajectory[:days+1,1]*1000
            z_true = true_trajectory[:days+1,2]*1000
            ufinal_baseline = np.array([x_true[-1],y_true[-1],z_true[-1]])
            err = np.linalg.norm(ufinal - ufinal_baseline)/np.linalg.norm(ufinal_baseline)
            err_vals.append(err)
    return err_vals

if __name__ == '__main__':
    bodies = ['asteroid_' + str(i) for i in range(5)]
    # bodies = []
    bodies.append('jupiter')
    bodies.append('earth')
    bodies.append('saturn')
    plot_traj(bodies, 365, plot_true=False)