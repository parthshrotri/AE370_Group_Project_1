import numpy as np
import matplotlib.pyplot as plt
from two_body_main import two_body_problem
from three_body_main import three_body_problem
from plotter import plot

def convergence_2b(days, tstep_vals):
    earth_err_vals = []
    for tstep in tstep_vals:
        two_body_problem(days, tstep)
        earth_err_vals.append(plot.error(['earth'])[0])
    return earth_err_vals
    
def convergence_3b(days, tstep_vals):
    earth_err_vals = []
    moon_err_vals = []
    for tstep in tstep_vals:
        three_body_problem(days, tstep)
        errors = plot.error(['earth, moon'])
        earth_err_vals.append(errors[0])
        moon_err_vals.append(errors[1])
    return earth_err_vals, moon_err_vals

if __name__ == '__main__':
    days = 365
    tsteps = np.logspace(np.log10(30), np.log10(60), 10)
    earth_two_body_err = convergence_2b(days, tsteps)
    earth_three_body_err, moon_three_body_err = convergence_3b(days, tsteps)
    
    plt.figure()
    plt.plot(tsteps, earth_two_body_err, label = "Earth Error")
    plt.legend()
    plt.title('Convergence of Two Body Problem')
    plt.xlabel('Timestep (s)')
    plt.ylabel('Global Error')
    plt.grid()
    
    plt.figure()
    plt.plot(tsteps, earth_three_body_err, 'b.', label = "Earth Error")
    plt.plot(tsteps, moon_three_body_err, 'k.', label = 'Moon Error')
    plt.legend()
    plt.title('Convergence of Three Body Problem')
    plt.xlabel('Timestep (s)')
    plt.ylabel('Global Error')
    plt.grid()
    plt.show()