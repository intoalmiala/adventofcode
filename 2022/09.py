from aocd import data
import re
import numpy as np

dirs = list(map(np.array, [(0, -1), (1, 0), (-1, 0), (0, 1)]))
dirmap = dict(zip("LDUR", dirs))

motions = [(dirmap[d], int(c)) for d, c in re.findall(r"(\w) (\d+)", data)]

def count_visited(N):
    ps = np.zeros((N,2), dtype=int)

    def near(p, q):
        return abs(p-q).max() <= 1

    visited = {tuple(ps[-1])}

    for dp, c in motions:
        for _ in range(c):
            ps[0] += dp
            for i in range(1, N):
                if near(ps[i-1], ps[i]):
                    continue
                ps[i] += np.sign(ps[i-1] - ps[i])
            visited.add(tuple(ps[-1]))
    return len(visited)

print(count_visited(2))
print(count_visited(10))
