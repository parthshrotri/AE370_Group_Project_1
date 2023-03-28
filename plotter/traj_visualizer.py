import glob, os
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tqdm import tqdm
import time

def get_trajectories_of_bodies(directory):
    os.chdir(directory)
    body_names = []
    appx_trajectories = {}
    for file in glob.glob("*.npy"):
        appx_trajectory = np.load(os.path.join(directory, file))
        body = file.replace('_trajectory.npy', '')
        body_names.append(body)
        appx_trajectories[body] = appx_trajectory
    return body_names, appx_trajectories

fig = plt.figure(figsize=(8, 10), tight_layout=True)
ax = fig.add_subplot(projection = '3d')
pts_per_frame = 10000

def animator(num, body_names, trajectories, graph_limits):
    ax.clear()
    ax.set_xticks(np.arange(graph_limits[0][0], graph_limits[0][1], 1E11).tolist())
    ax.set_yticks(np.arange(graph_limits[1][0], graph_limits[1][1], 1E11).tolist())
    ax.set_zticks(np.arange(graph_limits[2][0], graph_limits[2][1], 1E11).tolist())
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z', rotation = 0)
    ax.set_xlim(graph_limits[0][0], graph_limits[0][1])
    ax.set_ylim(graph_limits[1][0], graph_limits[1][1])
    ax.set_zlim(graph_limits[2][0], graph_limits[2][1])
    for body_name in body_names:
        x_body = trajectories[body_name][0:num*pts_per_frame+1][:,0]
        y_body = trajectories[body_name][0:num*pts_per_frame+1][:,1]
        z_body = trajectories[body_name][0:num*pts_per_frame+1][:,2]
        ax.plot(x_body, y_body, z_body, '-', label = body_name)
    ax.plot3D(0, 0, 0, '.', label='Sun', color='blue')
    ax.legend()

def run(with_jupiter: bool):
    start_time = time.time()
    str = ''
    if with_jupiter:
        str = 'with_jupiter'
    else:
        str = 'without_jupiter'
    directory = os.path.join(os.path.dirname(__file__),'..', 'output', str)

    body_names, trajectories = get_trajectories_of_bodies(directory)
    N = trajectories[body_names[0]].shape[0]
    print(N)
    animation = FuncAnimation(fig, animator, fargs=(body_names, trajectories), frames = N//pts_per_frame, interval=1, repeat=False)
    
    if with_jupiter:
        animation.save(os.path.join(directory, '../plots and graphs', 'orbits_with_jupiter.gif'), writer='Pillow', fps=100)
    else: 
        animation.save(os.path.join(directory, '../plots and graphs', 'orbits_without_jupiter.gif'), writer='Pillow', fps=100)
    
    print(time.time() - start_time)

if __name__ == '__main__':
    run(True)
    run(False)