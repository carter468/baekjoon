# 적의 적
# Gold 4, DFS

import sys
input = sys.stdin.readline

def dfs():
    visited = [0]*(n+1)
    for i in range(1,n+1):
        if visited[i] == 0:
            visited[i] = 1
            q = [(i,1)]
            while q:
                x,k = q.pop()
                for nx in graph[x]:
                    if visited[nx] == 0:
                        visited[nx] = -k
                        q.append((nx,-k))
                    elif visited[nx] == k:
                        return 0
    return 1

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs())