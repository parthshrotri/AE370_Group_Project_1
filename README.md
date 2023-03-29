# Tool for AnalYsis of ceLestial Orbits using RK4 in Series (TAYLOR Series)
Developed by Ieun Choo, Richeek Dutta, Myles Gong, Parth Shrotri, and Evan Yu
University of Illinois Urbana-Champaign Dept. of Aerospace Engineering

# Decription
The goal of TAYLOR Series is to provide a framework for analyzing celestial orbits using an $n$-body dynamical model. The Tool provides numerical analysis functionality to generate trajectories as well as options for easily plotting the results in a static or animated 3D format.

# Installing and Running TAYLOR Series
The code is written such that everything can be run from the `simulation` and `plot` folders. Use the `simulation` folder to write the main simulation functionality. Examples of TAYLOR Series usage can be found in `main.py`. Once the data is generated, the `plot` folder contains examples of using the plotting functionality to generate plots of the trajectories of all or some subset of the bodies in the simulation.

# Using TAYLOR Series
The main structure in TAYLOR Series is the `Body` class. This is where the dynamical system is defined. Each `Body` object contains information about one specific celstial object (e.g., Earth, Sun, Moon, etc.). This class performs all the dynamics calculations for each `Body` and returns the net force vector at each time step to be used by the RK4 function that propagates the system state over time. 

To visualize the data, there are two options. The first is contained in `plot.py` and generates static 3D plots of the data, i.e., it presents all the data at once and doe not change over time. This is useful for studying the entire trajectory and finding points where approximated solutions begin to diverge from true solutions. The other option is in `traj_visualization.py` and generates a .gif file with an animation for the trajectory. This is useful for visualizing how the trajectory of each object evolves over time and can provide a sense of how realistic the system solution is.

<img src="https://github.com/parthshrotri/AE370_Group_Project_1/blob/main/output/plots%20and%20graphs/orbits_with_jupiter_fast.gif" width="400" height="400"> <img src="https://github.com/parthshrotri/AE370_Group_Project_1/blob/main/output/plots%20and%20graphs/orbits_without_jupiter_fast.gif" width="400" height="400">
