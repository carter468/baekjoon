# 점심 나가서 먹기
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
        for dd,nx in graph[x]:
            nd = d+dd
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(q,(nd,nx))
    return dist

N,M = map(int,input().split())
X = tuple(map(int,input().split()))
Y = tuple(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

dist = dijkstra(1)

r = INF,0
c = INF,0
for i in range(2,N+1):
    if dist[i] == INF: continue
    if X[i-1] != 0 and X[i-1] < r[0]: r = X[i-1],i
    if Y[i-1] != 0 and Y[i-1] < c[0]: c = Y[i-1],i

dist1 = dijkstra(r[1])
print(dist[r[1]]+dist[c[1]]+dist1[c[1]])