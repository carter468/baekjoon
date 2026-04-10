# 철도계획
# Platinum 5, greedy, disjoint set

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,M = map(int,input().split())
R = sorted([tuple(map(int,input().split())) for _ in range(M)],key=lambda x:-x[2])

root = list(range(N+1))
cycle = [False]*(N+1)

t = 0
for u,v,w in R:
    u,v = find(u),find(v)
    if cycle[u] and cycle[v]: continue
    if u == v and cycle[u] == True: continue
    root[u] = v
    cycle[v] |= (u == v)|cycle[u]
    t += w
print(t)