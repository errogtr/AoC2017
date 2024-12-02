from itertools import combinations


with open("day02/data") as f:
    rows = [[int(x) for x in r.split("\t")] for r in f.read().splitlines()]

# PART 1
print(sum(max(r) - min(r) for r in rows))

# PART 2
print(sum(b // a for r in rows for a, b in combinations(sorted(r), 2) if b % a == 0))
