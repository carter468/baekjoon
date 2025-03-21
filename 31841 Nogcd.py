# Nogcd
# Gold 2, math, DFS

# DFS를 사용한 풀이

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global id
    visited[x] = True
    for nx,i in graph[x]:
        if result[i] == 0:
            result[i] = id
            id += 1
        if not visited[nx]:
            dfs(nx)

N,M = map(int,input().split())
edge = [tuple(map(int,input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
for i in range(M):
    u,v = edge[i]
    graph[u].append((v,i))
    graph[v].append((u,i))

result = [0]*M
id = 1
visited = [False]*(N+1)
dfs(1)

for i in range(M):
    print(*edge[i],result[i])


# Eulerian cycle(circuit)를 사용한 풀이

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
edge = [tuple(map(int,input().split())) for _ in range(M)]

graph = [set() for _ in range(N+1)]
for i in range(M):
    u,v = edge[i]
    graph[u].add((v,i))
    graph[v].add((u,i))

indegree = [0]*(N+1)
for u,v in edge:
    indegree[u] += 1
    indegree[v] += 1

odd = []
for i in range(1,N+1):
    if indegree[i]%2 == 1: odd.append(i)
for i in range(len(odd)//2):
    u,v = odd[i*2],odd[i*2+1]
    graph[u].add((v,M+i))
    graph[v].add((u,M+i))

id = 1
result = [0]*M
stack = [(1,M)]
while stack:
    x,_ = stack[-1]
    if graph[x]:
        nx,i = graph[x].pop()
        graph[nx].remove((x,i))
        stack.append((nx,i))
    else:
        _,i = stack.pop()
        if i < M:
            result[i] = id
            id += 1

for i in range(M):
    print(*edge[i],result[i])