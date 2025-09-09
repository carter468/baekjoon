# 그래프 탐험하기
# Gold 3, BFS, LCA, sparse table

from collections import deque
import sys
input = sys.stdin.readline

def dfs(v,p):
    up[v][0] = p
    for i in range(1,11):
        up[v][i] = up[up[v][i-1]][i-1]
    for to,_ in graph[v]:
        if to != p:
            depth[to] = depth[v]+1
            dfs(to,v)

def lca(a,b):
    if depth[a] < depth[b]:
        a,b = b,a

    diff = depth[a]-depth[b]
    for i in range(11):
        if diff&(1<<i):
            a = up[a][i]

    if a == b:
        return a

    for i in range(10,-1,-1):
        if up[a][i] != up[b][i]:
            a = up[a][i]
            b = up[b][i]

    return up[a][0]

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

edge = []
arr = []
q = deque([1])
dist = [-1]*(N+1)
dist[1] = 0
while q:
    x = q.popleft()
    arr.append(x)
    for nx,w in sorted(graph[x]):
        if dist[nx] == -1:
            dist[nx] = dist[x]+w
            q.append(nx)
            edge.append((x,nx,w))

graph = [[] for _ in range(N+1)]
for u,v,w in edge:
    graph[u].append((v,w))
    graph[v].append((u,w))
up = [[0]*11 for _ in range(N+1)]
depth = [0]*(N+1)
dfs(1,1)
lca_table = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        lca_table[i][j] = lca(i,j)

result = 0
x = arr[0]
i = 1
while i < N:
    nx = arr[i]
    l = lca_table[x][nx]
    result += dist[x]+dist[nx]-dist[l]*2
    i += 1
    x = nx
print(result+dist[x])