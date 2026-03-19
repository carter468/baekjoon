# Burnished Security Updates
# Gold 3, DFS

import sys
input = sys.stdin.readline
INF = 10**9

def dfs(i):
    color[i] = 0
    count = [1,0]
    q = [i]
    while q:
        x = q.pop()
        for nx in graph[x]:
            if color[x] == color[nx]:
                return INF
            if color[nx] == -1:
                color[nx] = 1-color[x]
                count[color[nx]] += 1
                q.append(nx)
    return min(count)

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0
color = [-1]*(N+1)
for i in range(1,N+1):
    if color[i] == -1:
        result += dfs(i)
print(result if result < INF else -1)