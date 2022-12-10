from aocd import data
import re
import numpy as np

dirs = list(map(np.array, [(0, -1), (1, 0), (-1, 0), (0, 1)]))
dirmap = dict(zip("LDUR", dirs))
motions = [(dirmap[d], int(c)) for d, c in re.findall(r"(\w) (\d+)", data)]

def count_visited(*tails):
    N = max(tails)
    ps = np.zeros((N,2), dtype=int)
    visited = {t: {tuple(ps[t-1])} for t in tails}

    for dp, c in motions:
        for _ in range(c):
            ps[0] += dp
            for i in range(1, N):
                if abs(ps[i-1] - ps[i]).max() <= 1:
                    continue
                ps[i] += np.sign(ps[i-1] - ps[i])
            for t in tails:
                visited[t].add(tuple(ps[t-1]))

    return *map(len, visited.values()),

print(*count_visited(2, 10))
