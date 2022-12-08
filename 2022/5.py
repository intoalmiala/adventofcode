from aocd import data
import re
from copy import deepcopy

init, steps = data.split("\n\n")

init = [line[1::4] for line in init.splitlines()[::-1][1:]]

stacks = [*zip(*init)]
stacks1 = [list(''.join(stack).strip()) for stack in stacks]
stacks2 = deepcopy(stacks1)

steps = [map(int, re.findall(r"\d+", line)) for line in steps.splitlines()]

for c, a, b in steps:
    stacks1[b-1].extend(stacks1[a-1][-1:-c-1:-1])
    del stacks1[a-1][-c:]
    stacks2[b-1].extend(stacks2[a-1][-c:])
    del stacks2[a-1][-c:]

print(''.join(stack[-1] for stack in stacks1))
print(''.join(stack[-1] for stack in stacks2))

