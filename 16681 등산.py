# 등산
# Gold 2, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    dist = [INF]*(N+1)
    dist[start] = 0
    q = [(0,start)]
    while q:
        d,x = heapq.heappop(q)
        if d > dist[x]: continue
        for nx,dd in graph[x]:
            nd = d+dd
            if h[nx] > h[x] and nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(q,(nd,nx))
    return dist

N,M,D,E = map(int,input().split())
h = [0]+list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,n = map(int,input().split())
    graph[a].append((b,n))
    graph[b].append((a,n))

dist1 = dijkstra(1)
dist2 = dijkstra(N)

result = -INF
for i in range(2,N):
    if dist1[i] != INF and dist2[i] != INF:
        result = max(result,h[i]*E-(dist1[i]+dist2[i])*D)
print(result if result != -INF else 'Impossible')