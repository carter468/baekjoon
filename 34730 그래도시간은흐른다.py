# 그래도 시간은 흐른다
# Gold 1, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

N,M,K,S,T = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,c,p = map(int,input().split())
    graph[u].append((v,c,p))

dist = [[INF]*K for _ in range(N+1)]
dist[S][0] = 0
q = [(0,S)]
while q:
    d,x = heapq.heappop(q)
    if d > dist[x][d%K]: continue
    for nx,c,p in graph[x]:
        nd = d+c
        if d%p == 0 and nd < dist[nx][nd%K]:
            dist[nx][nd%K] = nd
            heapq.heappush(q,(nd,nx))

result = min(dist[T])
print(result if result != INF else -1)