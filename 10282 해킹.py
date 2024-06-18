# 해킹
# Gold 4, dijkstra

import heapq,sys
input = sys.stdin.readline
INF = 10**9

for _ in range(int(input())):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((s,a))
    
    dist = [INF]*(n+1)
    dist[c] = 0
    q = [(0,c)]
    while q:
        d,x = heapq.heappop(q)
        if d > dist[x]: continue
        for dd,nx in graph[x]:
            nd = d+dd
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(q,(nd,nx))
    
    count,time = 0,0
    for d in dist:
        if d != INF:
            count += 1
            time = max(time,d)
    print(count,time)