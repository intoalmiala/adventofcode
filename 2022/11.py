from aocd import data
from math import lcm
from collections import namedtuple
from copy import deepcopy

Monkey = namedtuple("Monkey", "index items f modulo target")

monkeys = data.split("\n\n")
monkeys = [monkey.splitlines() for monkey in monkeys]
monkeys = [
    Monkey(
        int(index[7:-1]),
        list(map(int, items[18:].split(", "))),
        eval(operation[13:].replace("new =", "lambda old:")),
        int(modulo[21:]),
        (int(false[-1]), int(true[-1]))
    )
    for index, items, operation, modulo, true, false in monkeys
]

M = lcm(*[monkey.modulo for monkey in monkeys])

def simulate(monkeys, rounds, divisor):
    monkeys = deepcopy(monkeys)
    inspects = [0] * len(monkeys)

    for _ in range(rounds):
        for monkey in monkeys:
            inspects[monkey.index] += len(monkey.items)
            for item in monkey.items:
                item = monkey.f(item) % M // divisor
                target = monkey.target[item % monkey.modulo == 0]
                monkeys[target].items.append(item)
            monkey.items.clear()

    *_, a, b = sorted(inspects)
    return a*b

print(simulate(monkeys, 20, 3))
print(simulate(monkeys, 10000, 1))
