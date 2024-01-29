# Heat Wave
# Gold 5, dijkstra

import heapq

t,c,ts,te = map(int,input().split())

graph = [[] for _ in range(t+1)]
for _ in range(c):
    a,b,d = map(int,input().split())
    graph[a].append((d,b))
    graph[b].append((d,a))

distance = [10**9]*(t+1)
distance[ts] = 0
q = [(0,ts)]
while q:
    d,x = heapq.heappop(q)
    if d > distance[x]: continue
    for dd,nx in graph[x]:
        nd = d+dd
        if nd < distance[nx]:
            distance[nx] = nd
            heapq.heappush(q,(nd,nx))
print(distance[te])