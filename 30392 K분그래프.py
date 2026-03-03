# K분 그래프
# Gold 1, DFS

import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,w,x = map(int,input().split())
    graph[u].append((w,x))
    graph[w].append((u,x))

visited = [-1]*(N+1)
for i in range(1,N+1):
    if visited[i] == -1:
        visited[i] = 0
        q = [(i,0)]
        while q:
            x,d = q.pop()
            for nx,dd in graph[x]:
                nd = (d+dd)%K
                if visited[nx] == -1:
                    visited[nx] = nd
                    q.append((nx,nd))
                elif visited[nx] != nd:
                    exit(print('No'))
print('Yes')