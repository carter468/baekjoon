# 활자 그래프
# Gold 1, dijkstra

import sys,heapq
input = sys.stdin.readline

def dijkstra(s,e):
    dist = [10**19]*(N+1)
    dist[s] = 0
    q = [(0,s)]
    while q:
        d,x = heapq.heappop(q)
        if d > dist[x]: continue
        for dd,nx in graph[x]:
            nd = d+dd
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(q,(nd,nx))
    return dist[e]

T = int(input())
dist_arr = [[]]
for i in range(T):
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        v,w,x = map(int,input().split())
        if x >= 0: 
            graph[v].append((x,w))
        else: 
            graph[v].append((dist_arr[-x][0],w))
            graph[w].append((dist_arr[-x][1],v))
    
    dist_arr.append([dijkstra(1,2),dijkstra(2,1)])

print(dist_arr[-1][0] if dist_arr[-1][0] <= 10**18 else -1)