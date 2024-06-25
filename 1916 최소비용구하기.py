# 최소비용 구하기
# Gold 5, dijkstra

import sys,heapq
input = sys.stdin.readline

n,m = int(input()),int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
s,e = map(int,input().split())

dist = [10**9]*(n+1)
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
print(dist[e])