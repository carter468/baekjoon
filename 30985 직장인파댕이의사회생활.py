# 직장인 파댕이의 사회생활
# Gold 3, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m,k = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u,v,c = map(int,input().split())
    u,v = u-1,v-1
    graph[u].append((v,c))
    graph[v].append((u,c))
e = tuple(map(int,input().split()))

distance = [[INF]*2 for _ in range(n)]
distance[0][0] = 0
q = [(0,0,0)]
while q:
    d,x,y = heapq.heappop(q)
    if d > distance[x][y]: continue
    for nx,c in graph[x]:
        nd = d+c
        if nd < distance[nx][y]:
            distance[nx][y] = nd
            heapq.heappush(q,(nd,nx,y))
    if e[x] > 0 and y == 0:
        nd = d+e[x]*(k-1)
        if nd < distance[x][1]:
            distance[x][1] = nd
            heapq.heappush(q,(nd,x,1))

print(distance[-1][-1] if distance[-1][-1] != INF else -1)