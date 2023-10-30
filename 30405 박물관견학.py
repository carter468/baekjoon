# 박물관 견학
# Gold 5, greedy, math

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for _ in range(n):
    a = tuple(map(int,input().split()))
    arr.append(a[1])
    arr.append(a[-1])

print(sorted(arr)[n-1])