import numpy as np

#* Physical constants
hbar = 1 # Plank's constant, natural units

#* Constansts which are dictated by the physical setup
x_max = 1 # End of allowed x interval

#* Constants which are intrinsically our free choice
t_max = 1 # End of time interval on stopwatch
dx = 0.1 # x increment
dt = 0.1 # t increment

#* Constants which follow as a consequence
x_arr = np.arange(0, x_max + dx/2, dx)
t_arr = np.arange(0, t_max + dt/2, dt)