# DKSH를 찾아라
# Gold 5, DP

input()
d = k = s = h = 0
for c in input():
    if c == 'D':
        d += 1
    elif c == 'K':
        k += d
    elif c == 'S':
        s += k
    elif c == 'H':
        h += s
print(h)