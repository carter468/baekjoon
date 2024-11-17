# 출구가 바뀌는 미궁
# Gold 2, dijkstra

import sys,heapq
input = sys.stdin.readline

N,M,K = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
X = int(input())
E = tuple(map(int,input().split()))

dist = [sys.maxsize]*(N+1)
dist[1] = 0
q = [(0,1)]
while q:
    d,x = heapq.heappop(q)
    if d > dist[x]: continue
    for dd,nx in graph[x]:
        nd = d+dd
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(q,(nd,nx))

result = dist[0]
for i in range(X):
    d = dist[E[i]]
    a = (d-1)//(X*K)
    b = a*X*K+K*i
    if b <= d < b+K: b = d
    elif d >= b+K: b += X*K
    result = min(result,b)
print(result)