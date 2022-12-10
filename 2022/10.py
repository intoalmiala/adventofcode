from aocd import data
import re

inss = [0 if x == "noop" else int(x) for x in re.findall(r"(-?\d+|noop)", data)]

x = 1
cycles_left = 0
queue = iter(inss)
ins = 0
s = 0
crt = [[False] * 40 for _ in range(6)]

for i in range(0, 240):
    if not cycles_left:
        x += ins
        ins = next(queue)
        cycles_left = 1 + (ins != 0)
    cycles_left -= 1
    crt[i//40][i%40] = abs(i%40-x) <= 1
    if i % 40 == 19:
        s += (i+1)*x

print(s)

crt = '\n'.join([''.join(["—/"[x]*2 for x in row]) for row in crt])
print(crt)
