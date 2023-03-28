import glob, os
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tqdm import tqdm

directory = os.path.join(os.path.dirname(__file__),'..', 'output', 'without_jupiter')
earth_orbit_radius = 149E12 # m

def get_trajectories_of_bodies(with_jupiter: bool):
    str = ''
    if(with_jupiter):
        str = 'with_jupiter'
    else:
        str = 'without_jupiter'
    directory = os.path.join(os.path.dirname(__file__),'..', 'output', str)
    os.chdir(directory)
    body_names = []
    appx_trajectories = {}
    for file in glob.glob("*.npy"):
        appx_trajectory = np.load(os.path.join(directory, file))
        body = file.replace('_trajectory.npy', '')
        body_names.append(body)
        appx_trajectories[body] = appx_trajectory
    return body_names, appx_trajectories

def get_min_distance_from_earth(body_traj):
    orbit_radius = np.linalg.norm(body_traj, axis=1)
    min = np.min(np.abs(orbit_radius - np.ones_like(orbit_radius)*earth_orbit_radius))
    index_of_min = np.where(orbit_radius == min)
    return min, index_of_min

def get_traj_diff_percent(min_dist_with_jupiter, min_dist_without_jupiter):
    diff = min_dist_without_jupiter - min_dist_with_jupiter
    # norm_orig = np.linalg.norm(min_dist_with_jupiter)
    # print(norm_orig)
    return diff/min_dist_with_jupiter*100

def get_difference_in_traj_near_earth():
    '''Returns the difference in trajectories of the asteroids at their nearest approach to Earth's orbit
    
    Returns:
        percent_diff (list): List of the percent difference in trajectories of the asteroids at their nearest approach to Earth's orbit
        body_names (list): List of the names of the bodies
    '''
    body_names, appx_pos_with_jupiter = get_trajectories_of_bodies(True)
    body_names, appx_pos_without_jupiter = get_trajectories_of_bodies(False)
    earth_traj_with_jupiter = appx_pos_with_jupiter['earth']
    earth_traj_without_jupiter = appx_pos_without_jupiter['earth']
    percent_diff = []
    for body_name in body_names:
        with_jupiter = appx_pos_with_jupiter[body_name]
        without_jupiter = appx_pos_without_jupiter[body_name]

        diff_with, ind_with = get_min_distance_from_earth(with_jupiter)
        diff_without, ind_without = get_min_distance_from_earth(without_jupiter)

        percent_diff.append(get_traj_diff_percent(diff_with, diff_without))
    
    return percent_diff, body_names
    

percent_diff, body_names = get_difference_in_traj_near_earth()
for i in range(len(percent_diff)):
    if(body_names[i].startswith('asteroid')):
        print(f'{body_names[i]} percent difference: {percent_diff[i]}')