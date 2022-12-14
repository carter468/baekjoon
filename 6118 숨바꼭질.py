# 숨바꼭질
# Silver 1, 너비 우선 탐색

import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visit = [False]*(n+1)
depth = [0]*(n+1)
visit[1] = True
while q:
    x = q.popleft()
    for now in graph[x]:
        if not visit[now]:
            visit[now] = True
            depth[now] = depth[x]+1
            q.append(now)

answer = max(depth)
print(depth.index(answer),answer,depth.count(answer))