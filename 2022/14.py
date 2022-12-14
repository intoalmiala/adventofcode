from aocd import lines
import numpy as np

paths = [[eval(point) for point in line.split(" -> ")] for line in lines]
grid = np.full((300, 700), True)

ymax = 0
for path in paths:
    for (a, b), (c, d) in zip(path, path[1:]):
        if a > c or b > d:
            (a, b), (c, d) = (c, d), (a, b)
        grid[b:d+1, a:c+1] = False
        ymax = max(ymax, d)
grid[ymax+2, :] = False

def lower(y, x):
    yield y+1, x
    yield y+1, x-1
    yield y+1, x+1

p1 = False
i = 0
while grid[0, 500]:
    p = (0, 500)
    while (q := next(filter(grid.__getitem__, lower(*p)), p)) != p:
        p = q
    grid[p] = False
    if not p1 and p[0] > ymax:
        p1 = True
        print(i)
    i += 1
print(i)
