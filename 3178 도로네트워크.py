# 도로네트워크

from collections import deque
import sys,math
input = sys.stdin.readline

n = int(input())
l = int(math.log2(n))+1
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
parent = [[0,0] for _ in range(n+1)]
depth = [0]*(n+1)
visited = [False]*(n+1)
q = deque([1])
visited[1] = True
while q:
    x = q.popleft()
    for b,c in graph[x]:
        if visited[b] == False:
            q.append(b)
            depth[b] = depth[x] + 1
            visited[b] = True
            parent[b][0] = x
            parent[b][1] = c
dp = [[[0,0,0] for _ in range(l)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0][0] = parent[i][0]
    dp[i][0][1] = parent[i][1]
    dp[i][0][2] = parent[i][1]
for j in range(1,l):
    for i in range(1,n+1):
        dp[i][j][0] = dp[dp[i][j-1][0]][j-1][0]
        dp[i][j][1] = min(dp[i][j-1][1],dp[dp[i][j-1][0]][j-1][1])
        dp[i][j][2] = max(dp[i][j-1][2],dp[dp[i][j-1][0]][j-1][2])

k = int(input())
for _ in range(k):
    d,e = map(int,input().split())
    if depth[d] < depth[e]:
        d,e = e,d
    diff = depth[d] - depth[e]
    shortest = float('inf')
    longest = 0
    for i in range(l):
        if diff & 1<<i:
            shortest = min(shortest,dp[d][i][1])
            longest = max(longest,dp[d][i][2])
            d = dp[d][i][0]
    if d==e:
        print(shortest,longest)
        continue
    for i in range(l-1,-1,-1):
        if dp[d][i][0] != dp[e][i][0]:
            shortest = min(shortest,dp[d][i][1],dp[e][i][1])
            longest = max(longest,dp[d][i][2],dp[e][i][2])
            d = dp[d][i][0]
            e = dp[e][i][0]
    shortest = min(shortest,dp[d][i][1],dp[e][i][1])
    longest = max(longest,dp[d][i][2],dp[e][i][2])
    print(shortest,longest)