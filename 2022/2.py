from aocd import lines
parse = lambda line: line.translate(str.maketrans("ABC XYZ", "123-123"))
print(sum(
    eval(f"(1-({expr})%3)%3*3+int(expr[-1])")
    for line in lines
    if (expr := parse(line))
))
print(sum(
    d[expr[2]](int(expr[0]))
    for line in lines
    if (expr := parse(line))
    and (d := { '1': lambda x: 1+(x-2)%3
              , '2': lambda x: 3+x
              , '3': lambda x: 7+x%3
              })
))
