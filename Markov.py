from random import random

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

    while state != len(matrix):
        state = choice(matrix[state])
        states.append(state)
    
    return states