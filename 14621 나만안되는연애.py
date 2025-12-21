# 나만 안되는 연애
# Gold 3, MST

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,M = map(int,input().split())
G = input().split()
edge = []
for _ in range(M):
    u,v,d = map(int,input().split())
    if G[u-1] != G[v-1]:
        edge.append((d,u,v))

count = 1
result = 0
root = list(range(N+1))
for d,u,v in sorted(edge):
    u,v = find(u),find(v)
    if u != v:
        count += 1
        result += d
        root[u] = v

print(result if count == N else -1)