from itertools import pairwise

with open("day01/data") as f:
    digits = f.read()

# PART 1
first, *_ = digits
print(sum(int(a) for a, b in pairwise(digits + first) if a == b))

# PART 2
half = len(digits) // 2
print(sum(int(a) for a, b in zip(digits, digits[half:] + digits[:half]) if a == b))
