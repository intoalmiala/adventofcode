from aocd import lines

grid = {(y, x): c for y, line in enumerate(lines) for x, c in enumerate(line)}

goal,  = (p for p in grid if grid[p] == 'E')
start, = (p for p in grid if grid[p] == 'S')

grid[start], grid[goal] = 'a', 'z'

def neighbours(y, x):
    yield (y-1, x)
    yield (y+1, x)
    yield (y, x-1)
    yield (y, x+1)

queue, dist = [goal], {goal: 0}

for p in iter(queue):
    for q in neighbours(*p):
        if q in grid and q not in dist and ord(grid[p]) <= ord(grid[q]) + 1:
            dist[q] = dist[p] + 1
            queue.append(q)

print(dist[start])
print(min(dist[p] for p in dist if grid[p] == 'a'))
