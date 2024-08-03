# 106 miles to Chicago
# Gold 4, dijkstra

import sys,heapq
input = sys.stdin.readline

while True:
    a = input()
    if a[0] == '0': break
    n,m = map(int,a.split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,p = map(int,input().split())
        p /= 100
        graph[a].append((p,b))
        graph[b].append((p,a))
    
    percent = [0]*(n+1)
    percent[1] = -100
    q = [(-100,1)]
    while q:
        p,x = heapq.heappop(q)
        if p > percent[x]: continue
        for pp,nx in graph[x]:
            np = p*pp
            if np < percent[nx]:
                percent[nx] = np
                heapq.heappush(q,(np,nx))
    
    print(-percent[n],'percent')