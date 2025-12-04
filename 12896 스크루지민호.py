# 스크루지 민호
# Gold 2, BFS, tree diameter

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    visited = [-1]*(N+1)
    visited[start] = 0
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x]+1
                q.append(nx)
    return x,visited[x]

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

print((bfs(bfs(1)[0])[1]+1)//2)