from aocd import lines
p = {chr(x+ord('a')-1): x for x in range(1, 27)} | {chr(x+ord('A')-27): x for x in range(27, 53)}
print(sum(
    p[({*line[:l//2]} & {*line[l//2:]}).pop()]
    for line in lines
    if (l := len(line))
))
def f(s, xs):
    if not xs: return s
    a, b, c, *xs = xs
    return f(s+p[({*a} & {*b} & {*c}).pop()], xs)
print(f(0, lines))
