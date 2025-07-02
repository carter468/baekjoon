# Doomsday
# Gold 1, dijkstra

import sys,heapq
input = sys.stdin.readline

def dijkstra(s):
    dist = [sys.maxsize]*(N+2)
    dist[s] = 0
    q = [(0,s)]
    while q:
        d,x = heapq.heappop(q)
        if d > dist[x]: continue
        for dd,nx in graph[x]:
            nd = d+dd
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(q,(nd,nx))
    return dist

N,M,_,_ = map(int,input().split())
W = tuple(map(int,input().split()))
F = tuple(map(int,input().split()))
graph = [[] for _ in range(N+2)]
for _ in range(M):
    a,b,t = map(int,input().split())
    graph[a].append((t,b))
    graph[b].append((t,a))

dist = dijkstra(0)
p1,p2 = -1,-2
for w in W:
    t = dist[w]
    graph[p1].append((t,w))
for f in F:
    t = dist[f]
    graph[f].append((t,p2))
print(dijkstra(p1)[p2])