def sort(l):
    return ["".join(sorted(w)) for w in l]

with open("day04/data") as f:
    passphrases = [l.split() for l in f.readlines()]


print(sum(len(l) == len(set(l)) for l in passphrases))


print(sum(len(sort(l)) == len(set(sort(l))) for l in passphrases))

