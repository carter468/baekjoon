# 야쿠르트 아줌마 야쿠르트 주세요
# Gold 3, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))
seller = tuple(map(int,input().split()))
buyer = int(input())

limit = {seller[0]:0}
i = 1
result = 0
while i < 10:
    distance = [INF]*(V+1)
    distance[seller[i-1]] = 0
    q = [(0,seller[i-1])]
    while q:
        dist,node = heapq.heappop(q)
        if dist > distance[node]: continue
        for d,n in graph[node]:
            if dist+d < distance[n]:
                distance[n] = dist+d
                heapq.heappush(q,(distance[n],n))

    while i < 10 and distance[seller[i]] == INF:
        i += 1
    if i == 10: break
    result += distance[seller[i]]
    limit[seller[i]] = result
    i += 1

distance = [INF]*(V+1)
distance[buyer] = 0
q = [(0,buyer)]
while q:
    dist,node = heapq.heappop(q)
    if dist > distance[node]: continue
    for d,n in graph[node]:
        if dist+d < distance[n]:
            distance[n] = dist+d
            heapq.heappush(q,(distance[n],n))
result = INF
for i in limit:
    if distance[i] <= limit[i]:
        result = min(result,i)

print(result if result != INF else -1)