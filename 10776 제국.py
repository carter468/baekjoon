# 제국
# Gold 1, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

k,n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,t,h = map(int,input().split())
    graph[a].append((b,t,h))
    graph[b].append((a,t,h))
s,e = map(int,input().split())

distance = [[INF]*(k+1) for _ in range(n+1)]
distance[s][k] = 0
q = [(0,k,s)]
while q:
    d,p,node = heapq.heappop(q)
    if distance[node][p] < d: continue

    for nx,t,h in graph[node]:
        dd = d+t
        pp = p-h
        if pp > 0 and dd < distance[nx][pp]:
            distance[nx][pp] = dd
            heapq.heappush(q,(dd,pp,nx))

result = min(distance[e])
print(result if result != INF else -1)