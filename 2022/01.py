from aocd import data
calories = sorted(map(sum, [map(int, s.split()) for s in data.split("\n\n")]))
print(calories[-1])
print(sum(calories[-3:]))
