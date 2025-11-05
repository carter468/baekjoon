# Forbidden Turns
# Platinum 5, dijkstra

import sys,heapq
input = sys.stdin.readline

M,N,K = map(int,input().split())
S,E = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    x,y,c = map(int,input().split())
    graph[x].append((y,c))
FT = set([tuple(map(int,input().split())) for _ in range(K)])

dist = [dict() for _ in range(N)]
dist[S][0] = 0
q = [(0,S,0)]
while q:
    d,x,px = heapq.heappop(q)
    if d > dist[x][px]: continue
    for nx,dd in graph[x]:
        if (px,x,nx) in FT: continue
        nd = d+dd
        if x not in dist[nx] or nd < dist[nx][x]:
            dist[nx][x] = nd
            heapq.heappush(q,(nd,nx,x))

print(min([dist[E][x] for x in dist[E]]) if dist[E] else -1)