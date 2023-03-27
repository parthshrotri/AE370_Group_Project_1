import numpy as np
import matplotlib.pyplot as plt
from two_body_main import two_body_problem
from three_body_main import three_body_problem
from plotter import plot

def convergence_2b(days, tstep_vals):
    earth_err_vals = []
    time_vals = []
    for tstep in tstep_vals:
        time_vals.append(two_body_problem(days, tstep))
        earth_err_vals.append(plot.error(['earth'], 'two_body_test', days)[0])
    return earth_err_vals, time_vals
    
def convergence_3b(days, tstep_vals):
    earth_err_vals = []
    moon_err_vals = []
    time_vals = []
    for tstep in tstep_vals:
        time_vals.append(three_body_problem(days, tstep))
        errors = plot.error(['earth' , 'moon'], 'three_body_test', days)
        earth_err_vals.append(errors[0])
        moon_err_vals.append(errors[1])
    return earth_err_vals, moon_err_vals, time_vals

if __name__ == '__main__':
    days = 365
    t_min = 30
    t_max = 3600
    t_num = 20
    tsteps = np.logspace(np.log10(t_min), np.log10(t_max), t_num)
    earth_two_body_err, time_vals_two = convergence_2b(days, tsteps)
    # earth_three_body_err, moon_three_body_err, time_vals_three = convergence_3b(days, tsteps)
    
    plt.figure()
    plt.plot(tsteps, earth_two_body_err, 'b.', label = "Earth Error")
    plt.legend()
    plt.title('Convergence Test of Two Body Problem')
    plt.xlabel('Timestep (s)')
    plt.ylabel('Global Error')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid()
    
    # plt.figure()
    # plt.plot(tsteps, earth_three_body_err, 'b.', label = "Earth Error")
    # plt.plot(tsteps, moon_three_body_err, 'k.', label = 'Moon Error')
    # plt.legend()
    # plt.title('Convergence Test of Three Body Problem')
    # plt.xlabel('Timestep (s)')
    # plt.ylabel('Global Error')
    # plt.xscale('log')
    # plt.yscale('log')
    # plt.grid()

    plt.figure()
    plt.plot(tsteps, time_vals_two, 'r.', label = 'Runtime')
    plt.legend()
    plt.title('Runtime Comparison of Two Body Problem')
    plt.xlabel('Timestep(s)')
    plt.ylabel('Runtime')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid()

    # plt.figure()
    # plt.plot(tsteps, time_vals_three, 'r.', label = 'Runtime')
    # plt.legend()
    # plt.title('Runtime Comparison of Three Body Problem')
    # plt.xlabel('Timestep(s)')
    # plt.ylabel('Runtime')
    # plt.xscale('log')
    # plt.yscale('log')
    # plt.grid()

    plt.show()