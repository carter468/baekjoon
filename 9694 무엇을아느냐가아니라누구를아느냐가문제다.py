# 무엇을 아느냐가 아니라 누구를 아느냐가 문제다
# Gold 3, dijkstra

import sys,heapq
input = sys.stdin.readline

for i in range(int(input())):
    n,m = map(int,input().split())
    graph = [[] for _ in range(m)]
    for _ in range(n):
        x,y,z = map(int,input().split())
        graph[x].append((z,y))
        graph[y].append((z,x))
    
    dist = [99]*m
    dist[0] = 0
    q = [(0,0)]
    while q:
        d,x = heapq.heappop(q)
        if d > dist[x]: continue
        for dd,nx in graph[x]:
            nd = d+dd
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(q,(nd,nx))
    if dist[-1] == 99: result = [-1]
    else:
        result = [m-1]
        x = m-1
        while x != 0:
            for d,nx in graph[x]:
                if dist[nx]+d == dist[x]:
                    x = nx
                    result.append(nx)
                    break
    print(f'Case #{i+1}:',*result[::-1])
