# 나무나무나 심어야지
# Platinum 3, ETT, fenwick tree, offline query

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x):
    global idx
    idx += 1
    s[x] = idx
    for nx in graph[x]:
        dfs(nx)
    e[x] = idx

def update(i,dif):
    while i <= K:
        tree[i] += dif
        i += (i&-i)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

N,M = map(int,input().split())
K = N+M
graph = [[] for _ in range(K+2)]
for i,u in enumerate(map(int,input().split())):
    graph[u].append(i+1)
W = tuple(map(int,input().split()))
query = [tuple(map(int,input().split())) for _ in range(M)]

for q in query:
    if q[0] == 1:
        i,j = q[1],q[2]
        graph[i].append(j)
s = [0]*(K+1)
e = [0]*(K+1)
idx = 0
dfs(1)

tree = [0]*(K+1)
for i,w in enumerate(W):
    if w > 0:
        update(s[i+1],w)

for q in query:
    if q[0] == 1:
        j,w = q[2],q[3]
        if w > 0:
            update(s[j],w)
    else:
        i = q[1]
        x = prefix_sum(e[i])-prefix_sum(s[i]-1)
        print(x if x > 0 else -1)