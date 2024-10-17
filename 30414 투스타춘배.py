# 투스타 춘배
# Gold 3, DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    k = B[x-1]-A[x-1]
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            k += dfs(nx)
    return max(0,k)

n,p = map(int,input().split())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)
visited[p] = True
print(dfs(p))