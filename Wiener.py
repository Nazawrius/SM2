from math import floor, sin, pi
from random import gauss

import numpy as np
import matplotlib.pyplot as plt

def gen_process(M, dt):
    T = []
    for j in range(floor(1/dt) + 1):
        t = j * dt
        w = t*gauss(0, 1) + 2**0.5 * sum(sin(i*pi*t) / (i*pi) * gauss(0, 1) for i in range(1, M+1))
        T.append(w)
    
    return T

def plot_processes(processes, dt):
    t = [i*dt for i in range(floor(1/dt) + 1)]
    for process in processes:
        plt.plot(t, process, alpha=0.4)
    
    plt.show()

def approx_mean_var(process):
    return np.mean(process), np.mean(process)