# 이상적인 경로
# Platinum 5, BFS, traceback

from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    if a == b: continue
    graph[a].append((b,c))
    graph[b].append((a,c))

visited = [-1]*(N+1)
visited[N] = 0
q = deque([N])
while q:
    x = q.popleft()
    if x == 1: break
    for nx,_ in graph[x]:
        if visited[nx] == -1:
            visited[nx] = visited[x]+1
            q.append(nx)
print(visited[1])

result = []
arr = [1]
while True:
    m = 10**10
    narr = set()
    for x in arr:
        if x == N: exit(print(*result))
        for nx,c in graph[x]:
            if visited[nx]+1 == visited[x]:
                if c < m:
                    m = c
                    narr = {nx}
                elif c == m:
                    narr.add(nx)
    result.append(m)
    arr = narr