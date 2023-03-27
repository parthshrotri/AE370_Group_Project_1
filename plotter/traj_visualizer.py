import glob, os
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

directory = os.path.join(os.path.dirname(__file__),'..', 'output')

def get_trajectories_of_bodies(file_loc: str):
    os.chdir(directory)
    body_names = []
    appx_trajectories = {}
    for file in glob.glob(file_loc+"\*.npy"):
        appx_trajectory = np.load(os.path.join(os.path.dirname(__file__), '..','output', file))
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
        ax.plot(x_body, y_body, z_body, '-', label = body_name, linewidth = 1)
    ax.plot3D(0, 0, 0, '.', label='Sun', color='blue')
    ax.legend()

body_names, trajectories = get_trajectories_of_bodies('asteroid_test')
N = trajectories[body_names[0]].shape[0]
x_all, y_all, z_all = [], [], []
for body_name in body_names:
    x_all = x_all + trajectories[body_name][:, 0].tolist()
    y_all = y_all + trajectories[body_name][:, 1].tolist()
    z_all = z_all + trajectories[body_name][:, 2].tolist()
graph_limits = [[0.5E11 * math.floor(1.2*min(x_all)/0.5E11), 0.5E11 * math.ceil(1.2*max(x_all)/0.5E11)], [0.5E11 * math.floor(1.2*min(y_all)/0.5E11), 0.5E11 * math.ceil(1.2*max(y_all)/0.5E11)], [0.5E11 * math.floor(1.2*min(z_all)/0.5E11), 0.5E11 * math.ceil(1.2*max(z_all)/0.5E11)]]
animation = FuncAnimation(fig, animator, fargs=(body_names, trajectories, graph_limits), frames = N//pts_per_frame, interval=1, repeat=False)
animation.save(os.path.join(directory, 'plots and graphs', 'asteroid.gif'), writer='Pillow', fps=100)