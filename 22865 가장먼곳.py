# 가장 먼 곳
# Gold 4, dijkstra

import sys,heapq
input = sys.stdin.readline

n = int(input())
a,b,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    d,e,l = map(int,input().split())
    graph[d].append((e,l))
    graph[e].append((d,l))

result = []
for x in a,b,c:
    q = [(0,x)]
    dist = [sys.maxsize]*(n+1)
    dist[x] = 0
    while q:
        di,x = heapq.heappop(q)
        if dist[x] < di: continue
        for nx,d in graph[x]:
            nd = di+d
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(q,(nd,nx))
    result.append(dist)

answer = (0,-1)
for i in range(1,n+1):
    t = min(result[0][i],result[1][i],result[2][i])
    if t > answer[1]:
        answer = (i,t)
print(answer[0])