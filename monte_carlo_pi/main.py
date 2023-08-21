import multiprocessing
from math import sqrt
from random import random
from time import time

import numpy as np


def monte_carlo_pi():
    # initialize area, n
    n = 1000000
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
    t1 = time()
    with multiprocessing.Pool() as pool:
        print(f"Using {pool._processes} processes...")
        future_results = [pool.apply_async(monte_carlo_pi) for _ in range(1000)]
        results = [f.get() for f in future_results]
    t2 = time()
    print(f"Pi approximation is {np.average(results)}")
    print(f"Completed in {t2-t1}s")
