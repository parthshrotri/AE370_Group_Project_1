import numpy as np
import matplotlib.pyplot as plt
import os


fig = plt.figure(figsize=(8, 10), tight_layout=True)
ax = fig.add_subplot(111, projection='3d')
for filename in os.listdir(os.path.join(os.path.dirname(__file__), '..', 'data', 'npy_files')):
    if filename.endswith('.npy') and (filename.startswith('earth') or filename.startswith('moon')):
        data = np.load(os.path.join(os.path.dirname(__file__),  '..', 'data', 'npy_files', filename))
        print(data[:,0])
        x = data[:30,0]
        y = data[:30,1]
        z = data[:30,2]
        first_underscore = filename.index('_')
        ax.plot3D(x,y,z,'-', label=filename[:first_underscore])
# ax.plot3D(0, 0, 0, '.', label='Sun', color='yellow')
plt.legend() 
plt.xlabel('x [km]')
plt.ylabel('y [km]')
plt.show()