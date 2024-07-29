# 차트
# Gold 5, bruteforcing

import itertools

n = int(input())
arr = tuple(map(int,input().split()))
result = 0
for p in itertools.permutations(arr):
    count = 0
    for i in range(n):
        s = 0
        for j in range(n):
            s += p[(i+j)%n]
            if s == 50: count += 1
            if s >= 50: break
    result = max(result,count)
print(result//2)