# 전기가 부족해
# Gold 3, MST

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

n,m,k = map(int,input().split())
arr = tuple(map(int,input().split()))
edge = sorted([tuple(map(int,input().split())) for _ in range(m)],key=lambda x:x[2])

root = list(range(n+1))
for a in arr:
    root[a] = root[arr[0]]

result = 0
for u,v,w in edge:
    u,v = find(u),find(v)
    if u != v:
        root[u] = v
        result += w
print(result)
