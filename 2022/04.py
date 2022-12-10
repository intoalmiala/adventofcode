from aocd import lines
import re
from itertools import starmap
pairs = [tuple(map(int, re.findall(r"\d+", line))) for line in lines]
contained = lambda a, b, c, d: a <= c and d <= b or c <= a and b <= d
overlaps  = lambda a, b, c, d: c <= a <= d or a <= c <= b
print(sum(starmap(contained, pairs)))
print(sum(starmap(overlaps, pairs)))
