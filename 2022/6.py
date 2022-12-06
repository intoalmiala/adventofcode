from aocd import data
from itertools import takewhile
from more_itertools import windowed

def start_index(n):
    return len(list(takewhile(lambda l: len(set(l)) < n, windowed(data, n)))) + n

print(start_index(4))
print(start_index(14))
