from aocd import lines
import numpy as np

grid = np.array([[*line] for line in lines])
n, m = grid.shape

def findall(c):
    return [*zip(*np.where(grid == c))]

goal,  = findall('E')
start, = findall('S')
grid[start] = 'a'
grid[goal]  = 'z'

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def neighbours(y, x):
    for (dy, dx) in dirs:
        if 0 <= y+dy < n and 0 <= x+dx < m:
            yield (y+dy, x+dx)

queue = [goal]
d = np.zeros((n, m), dtype=int)
d[goal] = 1

for p in iter(queue):
    for q in neighbours(*p):
        if d[q] or ord(grid[p]) > ord(grid[q]) + 1:
            continue
        d[q] = d[p] + 1
        queue.append(q)

print(d[start]-1)
print(min(filter(None, [d[p] for p in findall('a')])) - 1)
