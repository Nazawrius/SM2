from math import log1p, exp, factorial
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

def plot_n_events(intensity, time, N):
    process_lens = [len(gen_process(intensity, time)) for _ in range(N)]
    
    plt.hist(process_lens, bins=20, rwidth=0.7)
    x = list(range(min(process_lens), max(process_lens)+1))
    y = list(map(lambda n: 3 * N * exp(-intensity*time) * (intensity*time)**n / factorial(n), x))
    plt.plot(x, y)
    plt.show()