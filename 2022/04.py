from aocd import lines
import re
from itertools import starmap

pairs = [tuple(map(int, re.findall(r"\d+", line))) for line in lines]

def contained(a, b, c, d):
    return a <= c and d <= b or c <= a and b <= d

def overlaps(a, b, c, d):
    return c <= a <= d or a <= c <= b

print(sum(starmap(contained, pairs)))
print(sum(starmap(overlaps, pairs)))
