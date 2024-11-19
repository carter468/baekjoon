# ENDLESS RAIN
# Gold 1, disjoint set

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,M = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(M)]

root = list(range(N+1))
result = 0
k = 0
for s,e in arr:
    k += 1
    e = find(e)
    while s < e:
        root[e] = find(e-1)
        e = find(e-1)
        if k: k -= 1
        else: result += 1

print(result)