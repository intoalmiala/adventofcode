from aocd import data
from itertools import starmap
from functools import cmp_to_key

def cmp(a, b):
    match a, b:
        case int(), int():
            return (a > b) - (a < b)
        case int(), list():
            return cmp([a], b)
        case list(), int():
            return cmp(a, [b])
        case list(), list():
            return next(filter(None, map(cmp, a, b)), cmp(len(a), len(b)))

lists = list(map(eval, data.split()))

pairs = list(zip(lists[::2], lists[1::2]))
print(sum((i+1) * (c<0) for i, c in enumerate(starmap(cmp, pairs))))

d1, d2 = [[2]], [[6]]
lists = sorted(lists + [d1, d2], key=cmp_to_key(cmp))
print((lists.index(d1)+1) * (lists.index(d2)+1))
