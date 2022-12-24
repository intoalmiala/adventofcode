from aocd import data
import re
from collections import defaultdict
from itertools import product

INF = 1e9
lines = re.findall(r".* (\w{2}) .*=(\d+).*valves? (.*)", data)
rate = {n: int(r) for n, r, _ in lines}
adj = {n: ns.split(", ") for n, _, ns in lines}

proper = [n for n in adj if rate[n]]
ind = {s: i for i, s in enumerate(proper)}
N = len(proper)
rate = {ind[n]: rate[n] for n in proper}

def dists(n):
    def dfs(s, p, d):
        dists = {}
        for t in adj[s]:
            if t == p: continue
            if t in proper:
                dists[t] = d+1
            else:
                dists.update(dfs(t, s, d+1))
        return dists
    return [(ind[b], d) for b, d in dfs(n, None, 0).items()]

adj = {ind[a]: dists(a) for a in proper} | {-1: dists('AA')}


def calculate_pressure(T=30):
    dp = [[[0] * 31 for _ in range(N)] for _ in range(2**N)]
    for x, w in adj[-1]:
        dp[1<<x][x][T-w-1] = rate[x]*(T-w-2) + 1
        dp[0][x][T-w] = 1

    for t in range(T, 0, -1):
        for k in range(N):
            for b in range(2**N):
                if not dp[b][k][t]:
                    continue
                if not (b>>k)&1:
                    dp[b | (1<<k)][k][t-1] = max(
                            dp[b | (1<<k)][k][t-1],
                            dp[b][k][t] + rate[k]*(t-1)
                    )
                for l, w in adj[k]:
                    if t-w < 0: continue
                    dp[b][l][t-w] = max(dp[b][l][t-w], dp[b][k][t])
    return dp

print(max(z for x in calculate_pressure(30) for y in x for z in y) - 1)

dp = calculate_pressure(26)
max_p = 0
maxs_s = sorted((max(y for x in dp[b] for y in x), b) for b in range(2**N))[1000:]
for (x, b), (y, d) in product(maxs_s, maxs_s):
    if b & d: continue
    max_p = max(max_p, x+y-2)
print(max_p)
