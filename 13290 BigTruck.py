# Big Truck
# Gold 3, dijkstra

import heapq
INF = 10**9

N = int(input())
T = tuple(map(int,input().split()))
graph = [[] for _ in range(N)]
for _ in range(int(input())):
    a,b,d = map(int,input().split())
    graph[a-1].append((d,b-1))
    graph[b-1].append((d,a-1))

q = [(0,0,T[0])]
dist = [(INF,0)]*N
dist[0] = [0,T[0]]
while q:
    d,x,c = heapq.heappop(q)
    if d > dist[x][0] or c < dist[x][1]: continue
    for dd,nx in graph[x]:
        nd = d+dd
        nc = c+T[nx]
        if nd < dist[nx][0]:
            dist[nx] = [nd,nc]
            heapq.heappush(q,(nd,nx,nc))
        elif nd == dist[nx][0] and nc > dist[nx][1]:
            dist[nx][1] = nc
            heapq.heappush(q,(nd,nx,nc))

if dist[-1][0] != INF:
    print(*dist[-1])
else:
    print('impossible')