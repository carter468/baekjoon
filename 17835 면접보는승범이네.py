# 면접보는 승범이네
# Gold 2, dijkstra

import sys,heapq
input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,c = map(int,input().split())
    graph[v].append((u,c))
arr = tuple(map(int,input().split()))

dist = [sys.maxsize]*(n+1)
for i in arr:
    dist[i] = 0
    q = [(0,i)]
    while q:
        d,x = heapq.heappop(q)
        if d > dist[x]: continue
        for nx,dd in graph[x]:
            nd = d+dd
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(q,(nd,nx))

result = [0,0]
for i in range(1,n+1):
    if dist[i] > result[0]: result = [dist[i],i]
print(result[1])
print(result[0])