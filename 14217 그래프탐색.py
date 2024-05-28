# 그래프 탐색
# Gold 5, BFS

from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for _ in range(int(input())):
    a,i,j = map(int,input().split())
    if a == 1:
        graph[i].append(j)
        graph[j].append(i)
    else:
        graph[i].remove(j)
        graph[j].remove(i)
    visited = [-1]*(n+1)
    visited[1] = 0
    q = deque([1])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x]+1
                q.append(nx)
    print(*visited[1:])