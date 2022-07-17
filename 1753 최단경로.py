# 최단경로

import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v,e = map(int,input().split())      # vertex, edge
k = int(input())                    # 시작정점

graph = [[] * (v+1) for _ in range(v+1)]  # i에서 j로의 간선  

INF = int(1e9)
distance = [INF]*(v+1)              # 최단거리

for _ in range(e):
    a,b,c = map(int,input().split())  
    graph[a].append((b,c))    

def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        a,b = heapq.heappop(q)  # 거리,정점
        if distance[b] < a:     # 이미 탐색된 상황
            continue
        for i in graph[b]:
            x = a+i[1]
            if x < distance[i[0]]:
                distance[i[0]] = x
                heapq.heappush(q,(x,i[0]))
        
dijkstra(k)

for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
