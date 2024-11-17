# 동까뚱뽭 게임
# Gold 3, DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    c = 0
    f = False
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            c += 1
            if not dfs(nx): f = True
    if c == 0: f = False
    result[x] = f
    return f

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

result = [-1]*(n+1)
visited = [False]*(n+1)
visited[1] = True
dfs(1)
for i in range(1,n+1):
    print('donggggas' if result[i] else 'uppercut')