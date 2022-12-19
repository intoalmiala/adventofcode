from aocd import lines
import re
from itertools import combinations
from collections import defaultdict

inf = int(1e9)

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def length(a, b):
    return b - a + 1

def cut(p, q):
    if None in {p, q}: return None
    a, b = max(p[0], q[0]), min(p[1], q[1])
    return (a, b) if a <= b else None

sensors = [
        [(int(a), int(b)) for a, b in re.findall(r"x=(-?\d+), y=(-?\d+)", line)]
        for line in lines
]
circles = {s: dist(*s, *b) for s, b in sensors}

level = 2000000

circles_on_level = {
    (x, y): r for (x, y), r in circles.items() if y-r <= level <= y+r
}
dxs = {
    (x, y): r - dr if r > (dr := abs(level-y)) else None
    for (x, y), r in circles_on_level.items()
}
intervals = [(x-dx, x+dx) for (x, y), dx in dxs.items() if dx is not None]

s = 0
for k in range(len(circles)):
    sign = k%2*2 - 1
    for comb in combinations(intervals, k):
        intersection = -inf, inf
        for interval in comb:
            intersection = cut(intersection, interval)
        if intersection not in {None, (-inf, inf)}:
            s += sign * length(*intersection)
s -= len({b for _, b in sensors if b[1] == level})

print(s)

cmin, cmax = 0, 4000000

diags = defaultdict(int)
for (x, y), r in circles.items():
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            a = x + j*(r+1) - y*i
            diags[i, a] += 1

for (k1, b1), (k2, b2) in combinations(diags, 2):
    if k1 == k2: continue
    if abs(b1 - b2) % 2: continue
    x = (b1 + b2) // 2
    y = abs(b1 - b2) // 2
    if cmin <= x <= cmax and cmin <= y <= cmax:
        if all(dist(x, y, *o) > r for o, r in circles.items()):
            print(cmax * x + y)
            break
