from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import os

def plot(bodies: list, days=20*365):
    
    planet_list = ['mercury', 'venus','earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'moon']
    

    fig = plt.figure(figsize=(8, 10), tight_layout=True)
    ax = fig.add_subplot( 111 , projection = '3d')
    for body in bodies:
        appx_trajectory = np.load(os.path.join(os.path.dirname(__file__), '..','output', body + '_trajectory.npy'))
        x = appx_trajectory[:,0]
        y = appx_trajectory[:,1]
        z = appx_trajectory[:,2]
        ax.plot3D(x,y,z,'-',label= body + ' Approximated Trajectory')
        ufinal = np.array([x[-1],y[-1],z[-1]])
        if body in planet_list:
            true_trajectory = np.load(os.path.join(os.path.dirname(__file__), '../data/npy_files', body + '_trajectory.npy'))
            x_true = true_trajectory[:days+1,0]*1000
            y_true = true_trajectory[:days+1,1]*1000
            z_true = true_trajectory[:days+1,2]*1000
            ax.plot3D(x_true, y_true, z_true,'-',label=body + ' True Trajectory')
            ufinal_baseline = np.array([x_true[-1],y_true[-1],z_true[-1]])
            err = np.linalg.norm(ufinal - ufinal_baseline)/np.linalg.norm(ufinal_baseline)
            print(f'Error in {body} trajectory: {err*100}%')
    
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