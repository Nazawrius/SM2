from math import floor, sin, pi
from random import gauss

import numpy as np
import matplotlib.pyplot as plt

def gauss_list(M):
    return [gauss(0, 1) for _ in range(M+1)]

def t(dt):
    t = []
    s = 0
    while s <= 1:
        t.append(s)
        s += dt
    return t

def gen_process(M, dt):
    T = []
    t = 0
    gl = gauss_list(M)
    while t <= 1:
        w = t*gl[0] + 2**0.5 * sum(sin(i*pi*t) / (i*pi) * gl[i] for i in range(1, M+1))
        T.append(w)
        t += dt
    
    return T

def plot_processes(processes, dt):    
    for process in processes:
        plt.plot(t(dt), process, alpha=0.4)
    
    plt.show()

def approx_mean_var(process):
    return np.mean(process), np.var(process)

def plot_mean_var(processes):
    means_and_vars = [approx_mean_var(process) for process in processes]
    means = [m for (m, _) in means_and_vars]
    vars = [v for (_, v) in means_and_vars]
    plt.hist(means, rwidth=0.7)
    plt.title("Means")
    plt.show()

    plt.hist(vars, rwidth=0.7)
    plt.title("Vars")
    plt.show()

    print("Global mean:", sum(means) / len(means))
    print("Mean variance:", sum(vars) / len(vars))

def plot_first_exit(processes, alpha, dt):
    first_exit = []
    times = t(dt)
    
    for process in processes:
        for (i, w) in enumerate(process):
            if w >= alpha:
                first_exit.append(times[i])
    
    plt.hist(first_exit, bins=20)
    plt.title("First exit")
    plt.show()