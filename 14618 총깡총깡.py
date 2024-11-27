# 총깡 총깡
# Gold 3, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = 10**9

N,M = map(int,input().split())
J = int(input())
K = int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    X,Y,Z = map(int,input().split())
    graph[X].append((Z,Y))
    graph[Y].append((Z,X))

dist = [INF]*(N+1)
dist[J] = 0
q = [(0,J)]
while q:
    d,x = heapq.heappop(q)
    if d > dist[x]: continue
    for dd,nx in graph[x]:
        nd = d+dd
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(q,(nd,nx))

r1,r2 = INF,INF
for a in A:
    r1 = min(r1,dist[a])
for b in B:
    r2 = min(r2,dist[b])

if (r1,r2) == (INF,INF): print(-1)
else:
    if r1 <= r2:
        print('A')
        print(r1)
    else:
        print('B')
        print(r2)