import glob, os
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tqdm import tqdm

directory = os.path.join(os.path.dirname(__file__),'..', 'output')

def get_trajectories_of_bodies():
    os.chdir(directory)
    body_names = []
    appx_trajectories = {}
    for file in glob.glob("*.npy"):
        appx_trajectory = np.load(os.path.join(os.path.dirname(__file__), '..','output', file))
        body = file.replace('_trajectory.npy', '')
        body_names.append(body)
        appx_trajectories[body] = appx_trajectory
    return body_names, appx_trajectories

fig = plt.figure(figsize=(8, 10), tight_layout=True)
ax = fig.add_subplot(projection = '3d')
pts_per_frame = 1000

def animator(num, body_names, trajectories):
    ax.clear()
    ax.set_xticks(np.linspace(-2E11, 6E11, 9).tolist())
    ax.set_yticks(np.linspace(-2E11, 8E11, 11).tolist())
    ax.set_zticks(np.linspace(-0.5E11, 2.5E11, 7).tolist())
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z', rotation = 0)
    ax.set_xlim(-2E11, 6E11)
    ax.set_ylim(-2E11, 8E11)
    ax.set_zlim(-1E11, 3E11)
    for body_name in body_names:
        x_body = trajectories[body_name][0:num*pts_per_frame+1][:,0]
        y_body = trajectories[body_name][0:num*pts_per_frame+1][:,1]
        z_body = trajectories[body_name][0:num*pts_per_frame+1][:,2]
        ax.plot(x_body, y_body, z_body, '.', label = body_name)
    ax.plot3D(0, 0, 0, '.', label='Sun', color='blue')
    ax.legend()

body_names, trajectories = get_trajectories_of_bodies()
N = trajectories[body_names[0]].shape[0]
animation = FuncAnimation(fig, animator, fargs=(body_names, trajectories), frames = N//pts_per_frame, interval=1, repeat=False)
animation.save(os.path.join(directory, 'plots and graphs', 'orbits.gif'), writer='Pillow', fps=100)