# Coolest Ski Route
# Gold 3, topological sorting

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    indegree[b] += 1

q = deque()
for i in range(1,n+1):
    if indegree[i] == 0: q.append(i)
result = [0]*(n+1)
while q:
    x = q.popleft()
    for nx,c in graph[x]:
        result[nx] = max(result[nx],result[x]+c)
        indegree[nx] -= 1
        if indegree[nx] == 0: q.append(nx)
print(max(result))