from random import random

import matplotlib.pyplot as plt

def choice(v):
    x = random()
    i = 0
    while i < len(v) - 1 and x > v[i]:
        x -= v[i]
        i += 1
    
    return i

def path(matrix, vector, length):
    state = choice(vector)
    states = [state]

    for _ in range(length):
        state = choice(matrix[state])
        states.append(state)
    
    return states

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

def plot_stationary(paths):
    x = list(range(5))
    comb = sum(paths, [])
    y = [comb.count(i) / len(comb) for i in range(5)]
    print(list(round(i, 3) for i in y))
    plt.bar(x, y)
    plt.show()