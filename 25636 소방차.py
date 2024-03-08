# 소방차
# Gold 2, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
water = tuple(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
s,e = map(int,input().split())

dist = [(INF,0)]*(n+1)
dist[s] = (0,0)
q = [(0,-water[s-1],s)]
while q:
    d,w,x = heapq.heappop(q)
    if (d,w) > dist[x]: continue
    for nx,dd in graph[x]:
        nd = d+dd
        nw = w-water[nx-1]
        if (nd,nw) < dist[nx]:
            dist[nx] = (nd,nw)
            heapq.heappush(q,(nd,nw,nx))

if dist[e][0] == INF: print(-1)
else: print(dist[e][0],-dist[e][1])