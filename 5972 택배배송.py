# 택배 배송
# Gold 5, dijkstra

import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

dist = [sys.maxsize]*(n+1)
dist[1] = 0
q = [(0,1)]
while q:
    d,x = heapq.heappop(q)
    if d > dist[x]: continue
    for dd,nx in graph[x]:
        nd = d+dd
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(q,(nd,nx))
print(dist[n])