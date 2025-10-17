# Candy Contribution
# Gold 4, dijkstra

import sys,heapq
input = sys.stdin.readline

N,M = map(int,input().split())
S,T,C = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,p = map(int,input().split())
    graph[u].append((v,p))
    graph[v].append((u,p))

dist = [0]*(N+1)
dist[S] = -C
q = [(-C,S)]
while q:
    d,x = heapq.heappop(q)
    if d > dist[x]: continue

    for nx,p in graph[x]:
        nd = -(-d*(100-p)//100)
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(q,(nd,nx))
print(-dist[T])