# 게임 개발
# Gold 3, topological sort

from collections import deque
import sys

n = int(input())
t = [0]
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for i in range(1,n+1):
    a = tuple(map(int,sys.stdin.readline().split()))
    t.append(a[0])
    for j in a[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

result = [0]*(n+1)
q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = t[i]
while q:
    x = q.popleft()
    for nx in graph[x]:
        result[nx] = max(result[nx],result[x]+t[nx])
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

for i in range(1,n+1):
    print(result[i])