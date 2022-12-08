from aocd import lines
import numpy as np
from itertools import starmap, product


grid = np.array([[*map(int, line)] for line in lines])


def views(y, x):
    return (grid[y-1:-1,x][::-1],
            grid[y+1:,x],
            grid[y,:x][::-1], 
            grid[y,x+1:])


def visible(y, x):
    def dmax(xs):
        return max(xs, default=-1)

    return grid[y,x] > min(map(dmax, views(y, x)))


coords = [*product(range(len(grid)), range(len(grid[0])))]

print(sum(starmap(visible, coords)))


def score(y, x):
    return np.prod([
        next(
            (i+1 for i, h in enumerate(v) if h >= grid[y,x]),
            len(v)
        ) for v in views(y, x)
    ])


print(max(starmap(score, coords)))

