# 와우 네트워크
# Gold 3, disjoint set

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,M,T = map(int,input().split())
arr = sorted([tuple(map(int,input().split())) for _ in range(M)],key=lambda x:x[2])

root = list(range(N+1))
t = 1
cnt = N
result = 0
for u,v,s in arr:
    u,v = find(u),find(v)
    result += (s-t)*cnt
    if u != v:
        root[u] = v
        cnt -= 1
    t = s
result += (T-t+1)*cnt
print(result)