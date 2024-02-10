# 달빛 여우
# Gold 1, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,d = map(int,input().split())
    graph[a].append((b,d*2))
    graph[b].append((a,d*2))

dist_fox = [INF]*(n+1)
dist_fox[1] = 0
q = [(0,1)]
while q:
    d,x = heapq.heappop(q)
    if d > dist_fox[x]: continue
    for nx,dd in graph[x]:
        nd = d+dd
        if nd < dist_fox[nx]:
            dist_fox[nx] = nd
            heapq.heappush(q,(nd,nx))

dist_wolf = [[INF]*2 for _ in range(n+1)]
q = [(0,1,1)]
while q:
    d,x,t = heapq.heappop(q)
    if d > dist_wolf[x][t]: continue
    for nx,dd in graph[x]:
        if t: dd //= 2
        else: dd *= 2
        nd = d+dd
        if nd < dist_wolf[nx][t^1]:
            dist_wolf[nx][t^1] = nd
            heapq.heappush(q,(nd,nx,t^1))
            
count = 0
for i in range(2,n+1):
    if dist_fox[i] < min(dist_wolf[i]): count += 1
print(count)