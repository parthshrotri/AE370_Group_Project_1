import glob, os
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
ax = fig.add_subplot( 111 , projection = '3d')
       
def animator(frame):
    body_names, trajectories = get_trajectories_of_bodies()
    num_indexes = len(trajectories[body_names[0]][:,0])
    # print(trajectories[body_names[0]][:9,0])
    line = []
    for index in range (num_indexes):
        # time.sleep(.1)
        # ax.clear()
        for body_name in body_names:
            # print(body_name)
            # print(trajectories[body_name])
            x_body = trajectories[body_name][:index+1,0]
            y_body = trajectories[body_name][:index+1,1]
            z_body = trajectories[body_name][:index+1,2]
            line_addition, = ax.plot(x_body, y_body, z_body, label = body_name)
            line.append(line_addition)
    print(line)
    return line,

animation = FuncAnimation(fig, animator, interval=500)
plt.show()
# animator()