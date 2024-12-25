# 배달하기
# Gold 1, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

N,M = map(int,input().split())
S,E = map(int,input().split())
K = int(input())
A = tuple(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

l = len(set(A))
dist = [INF]*(N+1)
dist[S] = 0
q = [(0,S)]
while q:
    t,x = heapq.heappop(q)
    if A[t%K] == x:
        if l == 1:
            dist[x] = INF
        else:
            heapq.heappush(q,(t+1,x))
            if dist[x] == t: dist[x] = t+1
        continue
    if t > dist[x]: continue
    for nx in graph[x]:
        if t+1 < dist[nx]:
            dist[nx] = t+1
            heapq.heappush(q,(t+1,nx))
print(dist[E] if dist[E] != INF else -1)