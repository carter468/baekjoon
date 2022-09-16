# LCA 2

import sys,math
from collections import deque
input = sys.stdin.readline

n = int(input())
l = int(math.log2(n))+1
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0]*(n+1)
depth = [0]*(n+1)
visited = [False]*(n+1)

q = deque()
q.append(1)
while q:
    x = q.popleft()
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            q.append(i)
            parent[i] = x
            depth[i] = depth[x] + 1

dp = [[0 for _ in range(l)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = parent[i]

for i in range(1,l):
    for j in range(1,n+1):
        dp[j][i] = dp[dp[j][i-1]][i-1]

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    if depth[a] > depth[b]:
        a,b = b,a
    d = depth[b]-depth[a]
    for i in range(l):
        if d & 1<<i:
            b = dp[b][i]
    if a == b:
        print(a)
    else:
        for i in range(l-1,-1,-1):
            if dp[a][i] != dp[b][i]:
                a = dp[a][i]
                b = dp[b][i]
        print(dp[b][0])