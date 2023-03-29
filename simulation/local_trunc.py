import numpy as np
from two_body_main import two_body_problem
from three_body_main import three_body_problem
import os
import matplotlib.pyplot as plt

baseline_delta_t = 30
delta_t_vals = np.logspace(np.log10(30), np.log10(3600), 20)

def two_body_local_trunc(delta_t, days, baseline_last):
    two_body_problem(days, delta_t, False)
    appx_traj = np.load(os.path.join(os.path.dirname(__file__), '../output/two_body_test/', 'earth_trajectory.npy'))
    appx_last = appx_traj[-1]
    err = np.linalg.norm(appx_last - baseline_last)/np.linalg.norm(baseline_last)
    return err

def two_body_baseline(baseline_delta_t, days = 365):
    two_body_problem(days, baseline_delta_t, False)
    baseline_traj = np.load(os.path.join(os.path.dirname(__file__), '../output/two_body_test/', 'earth_trajectory.npy'))
    baseline_last = baseline_traj[-1]
    return baseline_last

def three_body_local_trunc(delta_t, days, baseline_last):
    three_body_problem(days, delta_t, False)
    earth_appx_traj = np.load(os.path.join(os.path.dirname(__file__), '../output/three_body_test/', 'earth_trajectory.npy'))
    earth_appx_last = earth_appx_traj[-1]
    moon_appx_traj = np.load(os.path.join(os.path.dirname(__file__), '../output/three_body_test/', 'moon_trajectory.npy'))
    moon_appx_last = moon_appx_traj[-1]
    earth_err = np.linalg.norm(earth_appx_last - baseline_last[0])/np.linalg.norm(baseline_last[0])
    moon_err = np.linalg.norm(moon_appx_last - baseline_last[1])/np.linalg.norm(baseline_last[1])
    return [earth_err, moon_err]

def three_body_baseline(baseline_delta_t, days = 365):
    three_body_problem(days, baseline_delta_t, False)
    earth_baseline_traj = np.load(os.path.join(os.path.dirname(__file__), '../output/three_body_test/', 'earth_trajectory.npy'))
    earth_baseline_last = earth_baseline_traj[-1]
    moon_baseline_traj = np.load(os.path.join(os.path.dirname(__file__), '../output/three_body_test/', 'moon_trajectory.npy'))
    moon_baseline_last = moon_baseline_traj[-1]
    baseline_last = [earth_baseline_last, moon_baseline_last]
    return baseline_last

days = 365
two_body_errors = []
earth_three_body_errors, moon_three_body_errors = [], []
ctr = 1
two_body_baseline_last = two_body_baseline(baseline_delta_t, days)
three_body_baseline_last = three_body_baseline(baseline_delta_t, days)
for delta_t in delta_t_vals:
    two_body_errors.append(two_body_local_trunc(delta_t, days, two_body_baseline_last))
    three_error = three_body_local_trunc(delta_t, days, three_body_baseline_last)
    earth_three_body_errors.append(three_error[0])
    moon_three_body_errors.append(three_error[1])
    print(ctr)
    ctr += 1

plt.figure()
plt.plot(delta_t_vals, delta_t_vals**4, '-', label = '$\Delta t^4$')
plt.plot(delta_t_vals, two_body_errors, '-', label = 'Earth error')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('timestep $\Delta$ t')
plt.ylabel('Local truncation error')
plt.title('Local truncation error vs $\Delta$ t for 2-body problem')
plt.legend()

plt.figure()
plt.plot(delta_t_vals, delta_t_vals**4, '-', label = '$\Delta t^4$')
plt.plot(delta_t_vals, earth_three_body_errors, '-', label = 'Earth error')
plt.plot(delta_t_vals, moon_three_body_errors, '-', label = 'Moon error')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('timestep $\Delta$ t')
plt.ylabel('Local truncation error')
plt.title('Local truncation error vs $\Delta$ t for 3-body problem')
plt.legend()
plt.show()