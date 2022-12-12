from aocd import lines
import numpy as np
from functools import lru_cache

dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
grid = np.array([[*map(ord, line)] for line in lines])
n, m = grid.shape

def find(c):
    return [*zip(*np.where(grid == ord(c)))]

goal  = find('E')[0]
start = find('S')[0]
grid[start] = ord('a')
grid[goal]  = ord('z')

def shortest_path(start, goal):
    @lru_cache()
    def neighbors(y, x):
        return [
            (y+dy, x+dx)
            for (dy, dx) in dirs
            if  0 <= y+dy < n
            and 0 <= x+dx < m
            and grid[y+dy,x+dx] <= grid[y,x] + 1
        ]

    queue = [start]
    d = np.zeros((n, m), dtype=int)
    d[start] = 1

    for p in iter(queue):
        if p == goal:
            return d[p]-1
        for q in neighbors(*p):
            if d[q]: continue
            d[q] = d[p] + 1
            queue.append(q)

    return 1_000_000_000

print(shortest_path(start, goal))
print(min(shortest_path(p, goal) for p in find('a')))
