# 한국의 철도
# Gold 3, dijkstra, combinatorics

import sys,heapq
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    s,e,d = map(int,input().split())
    graph[s].append((e,d))
    graph[e].append((s,d))
P = tuple(map(int,input().split()))

dist = [10**15]*(N+1)
dist[1] = 0
q = [(0,1)]
while q:
    d,x = heapq.heappop(q)
    if d > dist[x]: continue
    for nx,dd in graph[x]:
        nd = d+dd
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(q,(nd,nx))

heap = []
for i in range(1,N+1):
    heapq.heappush(heap,(-dist[i],-P[i-1]))

result = 0
while heap:
    d,p = heapq.heappop(heap)
    c = 1
    while heap and (d,p) == heap[0]:
        heapq.heappop(heap)
        c += 1
    result += c*len(heap)
print(result,result)