# Mania de Par
# Gold 2, dijkstra

import sys,heapq
input = sys.stdin.readline

C,V = map(int,input().split())
graph = [[] for _ in range(C+1)]
for _ in range(V):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dist = [[10**9]*2 for _ in range(C+1)]
dist[1][0] = 0
q = [(0,1,0)]
while q:
    d,x,c = heapq.heappop(q)
    if d > dist[x][c]: continue

    nc = c^1
    for nx,dd in graph[x]:
        nd = d+dd
        if nd < dist[nx][nc]:
            dist[nx][nc] = nd
            heapq.heappush(q,(nd,nx,nc))

print(dist[C][0] if dist[C][0] < 10**9 else -1)