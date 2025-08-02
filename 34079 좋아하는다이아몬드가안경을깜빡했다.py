# 좋아하는 다이아몬드가 안경을 깜빡했다
# Gold 1, BFS

from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    visited = [-1]*(N+1)
    visited[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x]+1
                q.append(nx)
    return visited

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

v1 = bfs(1)
v2 = bfs(N)

arr = [set() for _ in range(N+1)]
for i in range(2,N):
    if v1[i]+v2[i] == v1[N]:
        arr[v1[i]].add(i)

for i in range(N):
    if len(arr[i]) == 1:
        print(*arr[i])
        break
else: print(1)