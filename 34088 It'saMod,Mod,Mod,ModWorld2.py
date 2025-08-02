# It's a Mod, Mod, Mod, Mod World 2
# Platinum 3, math, randomization

import random
from collections import defaultdict

if input() == '1': exit(print(1))
A = tuple(map(int,input().split()))

result = 1
for _ in range(99):
    a,b = random.sample(A,2)
    d = abs(a-b)
    f = set()
    i = 2
    while i*i <= d:
        while d%i == 0:
            f.add(i)
            d //= i
        i += 1
    if d > 1: f.add(d)

    for x in f:
        count = defaultdict(int)
        for a in A:
            r = a%x
            count[r] += 1
            result = max(result,count[r])
print(result)