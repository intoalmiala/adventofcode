from aocd import lines
from dataclasses import dataclass
from collections import defaultdict
from operator import methodcaller
from pathlib import Path
from functools import lru_cache

@dataclass(unsafe_hash=True)
class File:
    size: int
    path: str

contents = defaultdict(list)
wd = Path('/')

for t, name, *args in map(methodcaller('split'), lines):
    if t == '$':
        if name == 'ls': continue
        wd = (wd / args[0]).resolve()
    elif t == 'dir':
        contents[wd].append(wd / name)
    else:
        contents[wd].append(File(int(t), name))


@lru_cache
def size(d):
    if isinstance(d, File):
        return d.size
    return sum(map(size, contents[d]))

sizes = list(map(size, contents))

print(sum(filter(lambda s: s <= 100000, sizes)))
print(next(s for s in sorted(sizes) if 70000000-(size(Path('/'))-s) >= 30000000))
