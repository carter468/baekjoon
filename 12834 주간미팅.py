# 주간 미팅
# Gold 4, 데이크스트라

import heapq
import sys
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    distance = [INF]*(V+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,x = heapq.heappop(q)
        for d,nx in graph[x]:
            k = dist + d
            if k < distance[nx]:
                distance[nx] = k
                heapq.heappush(q,(k,nx))
    
    result = 0
    for x in team:
        result += distance[x] if distance[x]!=INF else -1
    return result

N,V,E = map(int,input().split())    # 팀원, 정점, 간선
A,B = map(int,input().split())      # KIST, 씨알푸드

team = tuple(map(int,input().split()))
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,l = map(int,input().split())
    graph[a].append((l,b))
    graph[b].append((l,a))

print(dijkstra(A)+dijkstra(B))