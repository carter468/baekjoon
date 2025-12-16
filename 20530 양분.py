# 양분
# Platinum 5, DFS, disjoint set

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,Q = map(int,input().split())
graph = [set() for _ in range(N+1)]
for _ in range(N):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

root = list(range(N+1))
q = []
for i in range(1,N+1):
    if len(graph[i]) == 1:
        q.append(i)
while q:
    x = q.pop()
    nx = graph[x].pop()
    root[find(x)] = find(nx)
    graph[nx].remove(x)
    if len(graph[nx]) == 1:
        q.append(nx)

for _ in range(Q):
    u,v = map(int,input().split())
    print(1 if find(u) == find(v) else 2)