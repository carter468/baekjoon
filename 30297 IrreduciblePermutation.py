# Irreducible Permutation
# Gold 4, ad hoc

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = tuple(map(int,input().split()))

    result = [0,[]]
    t = 0
    for i in range(n-1):
        t = max(t,arr[i])
        if t == i+1:
            result[0] += 1
            result[1].append(i+1)
            
    print(result[0])
    if result[0]: print(*result[1])