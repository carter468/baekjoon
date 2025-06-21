# 주말 여행 계획
# Gold 1, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = 10**9

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]
P,Q = map(int,input().split())

dist = [-INF]*(N+1)
q = []
for _ in range(P):
    l,w = map(int,input().split())
    dist[l] = w
    heapq.heappush(q,(-w,l))

while q:
    d,x = heapq.heappop(q)
    if -d < dist[x]: continue

    for nx in range(1,N+1):
        if arr[x-1][nx-1] == 0: continue
        nd = -d-arr[x-1][nx-1]
        if nd > dist[nx]:
            dist[nx] = nd
            heapq.heappush(q,(-nd,nx))

result = -INF
for _ in range(Q):
    l,w = map(int,input().split())
    result = max(result,dist[l]+w)
print(result)