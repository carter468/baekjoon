# 편의점
# Gold 3, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
input()
A = set(map(int,input().split()))
B = set(map(int,input().split()))

dist = [INF]*(n+1)
q = []
for i in B: heapq.heappush(q,(0,i))
while q:
    d,x = heapq.heappop(q)
    if x in A:
        print(x)
        break
    if dist[x] < d: continue
    for nx,dd in graph[x]:
        nd = d+dd
        if nx not in B and nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(q,(nd,nx))