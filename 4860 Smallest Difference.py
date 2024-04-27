# Smallest Difference
# Gold 5, bruteforcing

import itertools

for _ in range(int(input())):
    arr = input().split()
    l = len(arr)//2
    result = 10**9
    for p in itertools.permutations(arr):
        a = int(''.join(p[:l]))
        b = int(''.join(p[l:]))
        if (p[0] == '0' and a != 0) or (p[l] == '0' and b != 0): continue 
        result = min(result,abs(a-b))
    print(result)