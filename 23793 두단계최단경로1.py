# 두 단계 최단 경로 1
# Gold 4, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
x,y,z = map(int,input().split())

def dijkstra(s,e,b):
    dist = [INF]*(n+1)
    dist[s] = 0
    q = [(0,s)]
    while q:
        d,node = heapq.heappop(q)
        if dist[node] < d: continue
        for now,di in graph[node]:
            if now == b: continue
            nd = d+di
            if nd < dist[now]:
                dist[now] = nd
                heapq.heappush(q,(nd,now))
    return dist[e]

r1 = dijkstra(x,y,0)
r2 = dijkstra(y,z,0)
r3 = dijkstra(x,z,y)
print(-1 if r1 == INF or r2 == INF else r1+r2, -1 if r3 == INF else r3)