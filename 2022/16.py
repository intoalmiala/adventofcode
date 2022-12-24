from aocd import data
import re
from collections import defaultdict
from itertools import product

#data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
#Valve BB has flow rate=13; tunnels lead to valves CC, AA
#Valve CC has flow rate=2; tunnels lead to valves DD, BB
#Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
#Valve EE has flow rate=3; tunnels lead to valves FF, DD
#Valve FF has flow rate=0; tunnels lead to valves EE, GG
#Valve GG has flow rate=0; tunnels lead to valves FF, HH
#Valve HH has flow rate=22; tunnel leads to valve GG
#Valve II has flow rate=0; tunnels lead to valves AA, JJ
#Valve JJ has flow rate=21; tunnel leads to valve II"""

INF = 1e9
lines = re.findall(r".* (\w{2}) .*=(\d+).*valves? (.*)", data)
rate = {n: int(r) for n, r, _ in lines}
adj = {n: ns.split(", ") for n, _, ns in lines}

proper = [n for n in adj if rate[n]]
ind = {s: i for i, s in enumerate(proper)}
N = len(proper)
rate = {ind[n]: rate[n] for n in proper}

# TODO: tee leveyshaku
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

#def paths(t):
#    def dfs(a, p, t, opened):
#        #print("-> ", a, p, t)
#        if t <= 0:
#            return {}
#        paths = defaultdict(int)
#        a_is_open = a == 0 or (opened >> a)&1
#        opened_a = opened | (1<<a)
#        for (b, w) in adj[a]:
#            if not a_is_open:
#                paths[a] = max(paths[a], rate[a]*(t-1))
#                paths.update({
#                    x: max(paths[x], y)
#                    for x, y in dfs(b, a, t-1-w, opened_a).items()
#                })
#                #paths[opened_a] = max(
#                #    paths[opened_a],
#                #    rate[a]*(t-1) + dfs(b, a, t-w-1, opened_a)
#                #)
#            elif b != p:
#                paths.update({
#                    x: max(paths[x], y)
#                    for x, y in dfs(b, a, t-w, opened).items()
#                })
#                #paths[opened] = max(paths[opened], dfs(b, a, t-w, opened))
#        #print("<- ", a, p, t)
#        #if t > 1 and not a_is_open:
#        #    print(a, rate[a]*(t-1), paths)
#        #    input()
#        #if max_p > 1000: print(max_p)
#        return paths
#    return dfs(0, None, t, 0)

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
#dp30 = calculate_pressure(30)
#dp26 = calculate_pressure(26)
#max_p = 0
#max1 = 0
#mask = 2**N - 1
#for b in range(2**N):
#    max1 = max(max1, max(y for x in dp30[b] for y in x))
#    d = b^mask
#    max_b = max(y for x in dp26[b] for y in x) - 1
#    max_d = max(y for x in dp26[d] for y in x) - 1
#    max_p = max(max_p, max_b + max_d)
#print(max1 - 1)
#print(max_p)

dp = calculate_pressure(26)
max_p = 0
maxs_s = sorted((max(y for x in dp[b] for y in x), b) for b in range(2**N))[1000:]
for (x, b), (y, d) in product(maxs_s, maxs_s):
    if b & d: continue
    max_p = max(max_p, x+y-2)
print(max_p)
