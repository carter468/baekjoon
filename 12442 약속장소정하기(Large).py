# 약속장소 정하기 (Large)
# Gold 4, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = 10**9

for t in range(int(input())):
    N,P,M = map(int,input().split())
    arr = [tuple(map(int,input().split())) for _ in range(P)]
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        d,l,*a = map(int,input().split())
        for i in range(l-1):
            u,v = a[i],a[i+1]
            graph[u].append((v,d))
            graph[v].append((u,d))
    
    result = [0]*(N+1)
    for x,v in arr:
        q = [(0,x)]
        dist = [INF]*(N+1)
        dist[x] = 0
        while q:
            d,x = heapq.heappop(q)
            if d > dist[x]: continue
            for nx,dd in graph[x]:
                nd = d+dd*v
                if nd < dist[nx]:
                    dist[nx] = nd
                    heapq.heappush(q,(nd,nx))
        for i in range(1,N+1):
            result[i] = max(result[i],dist[i])
    
    if (m := min(result[1:])) == INF: m = -1
    print(f'Case #{t+1}: {m}')