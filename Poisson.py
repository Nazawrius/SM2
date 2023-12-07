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
        plt.step(events, range(len(events), label=f"Realization #{i}"))
    
    plt.xlabel("Time")
    plt.ylabel("Number of events")
    plt.legend()
    plt.show()
