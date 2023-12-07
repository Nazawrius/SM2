from math import log1p
from random import random

def gen_process(intensity, time):
    events = []
    
    t = 0
    while t < time:
        event = -log1p(-random()) / intensity
        t += event
        if t < time:
            events.append(event)
    
    return events