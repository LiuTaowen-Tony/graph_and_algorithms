from functools import combinations

def powerset(s : set):
    return set(combinations(s, r) for r in range(len(s) + 1))

def BHK(nodes : set[int], W : list[list[int]]):
    start = 1
    c = dict()

    for x in nodes:
        key = (set(), x)
        c[key] = W[start][x]

    for S in powerset(nodes - {start}):
        for x in nodes - (S | {start}):
            c[(S, x)] = 99999
        for y in S:
            c[(S, x)] = min(c[(S - [y], y)] + W[y][x], c[S, x])

    opt = 99999
    for x in nodes - {start}:
        opt = min(c[(nodes - {start, x}, x)] + W[x][start], opt)

    return opt