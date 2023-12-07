from math import log1p
from random import random

import matplotlib.pyplot as plt

def gen_process(intensity, time):
    events = []
    
    t = 0
    while t < time:
        step = -log1p(-random()) / intensity
        t += step
        if t < time:
            events.append(t)
    
    return events

def plot_processes(processes):
    for (i, events) in enumerate(processes):
        plt.step(events, range(len(events)), label=f"Realization #{i}")
    
    plt.xlabel("Time")
    plt.ylabel("Number of events")
    plt.legend()
    plt.show()

def plot_num_vs_time(process):
    plt.bar(range(len(process)), process)
    plt.xlabel("Event number")
    plt.ylabel("Time")
    plt.show()

def plot_diff(process):
    diff = [process[i+1] - process[i] for i in range(len(process) - 1)]
    plt.bar(range(len(diff)), diff)
    plt.xlabel("Event number")
    plt.ylabel("Event interval")
    plt.show()
