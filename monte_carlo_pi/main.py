from random import random
from math import sqrt
import time


def monte_carlo_pi(n=100):
    # initialize area
    inside, outside = 0, 0
    # Simulate area
    for _ in range(n):
        x, y = random(), random()
        res = sqrt(x**2 + y**2)
        if res < 1:
            inside += 1
        else:
            outside += 1
    # Calculate pi, inside = (pi*r^2)/4
    pi = inside * 4 / n
    return pi


if __name__ == "__main__":
    pass
