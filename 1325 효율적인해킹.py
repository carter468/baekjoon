# 효율적인 해킹

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    c = 1
    visited = [False]*(n+1)
    visited[x] = True
    q = deque([x])
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                c += 1
    return c

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
ans = []
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
max_value = 0
for i in range(1,n+1):
    cnt = bfs(i)
    if cnt >= max_value:
        ans.append([i,cnt])
        max_value = cnt
for i,cnt in ans:
    if cnt == max_value:
        print(i,end=' ')