from random import random

import matplotlib.pyplot as plt

def choice(v):
    x = random()
    i = 0
    while i < len(v) - 1 and x > v[i]:
        x -= v[i]
        i += 1
    
    return i

def path(matrix, vector):
    state = choice(vector)
    states = [state]

    while state != len(matrix) - 1:
        state = choice(matrix[state])
        states.append(state)
    
    return states + [state]

def plot_paths(paths):
    for path in paths:
        n = list(range(len(path)))
        plt.plot(n, path)
        plt.show()

def experimental_matrix(paths):
    exp_m = [[[0, 0] for _ in range(5)] for j in range(5)]

    for path in paths:
        for i in range(len(path) - 1):
            for j in range(5):
                exp_m[path[i]][j][1] += 1
            exp_m[path[i]][path[i+1]][0] += 1
        
    for i in range(5):
        for j in range(5):
            exp_m[i][j] = round(exp_m[i][j][0] / exp_m[i][j][1], 2) if exp_m[i][j][1] != 0 else 0.0
    
    return exp_m

def experimental_consecutive_time(paths):
    exp_t = [[0, 0] for _ in range(5)]
    for path in paths:
        for i in range(5):
            exp_t[i][0] += path.count(i)
        
        for i in range(len(path) - 1):
            if path[i+1] != path[i]:
                exp_t[path[i]][1] += 1
        exp_t[path[-1]][1] += 1    
    
    for i in range(5):
        exp_t[i] = round(exp_t[i][0] / exp_t[i][1], 2)
    
    return exp_t

def mean_absorbsion_time(paths):
    return sum(len(path) - 2 for path in paths) / len(paths)