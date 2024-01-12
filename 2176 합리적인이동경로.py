# 합리적인 이동경로
# Gold 2, dijkstra, DP

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

distance = [INF]*(n+1)
dp = [0]*(n+1)
distance[2],dp[2] = 0,1
q = [(0,2)]
while q:
    d,x = heapq.heappop(q)
    if d > distance[x]: continue
    for dd,xx in graph[x]:
        nd = d+dd
        if nd < distance[xx]:
            distance[xx] = nd
            heapq.heappush(q,(nd,xx))
        if distance[xx] < d:
            dp[x] += dp[xx]
print(dp[1])