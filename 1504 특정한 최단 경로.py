# 특정한 최단 경로

import heapq    
import sys
input = sys.stdin.readline

# 입력
n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v1,v2 = map(int,input().split()) 

#데이크스트라 알고리즘 
def dijkstra(start,end): 
    distance = [inf]*(n+1)
    distance[start] = 0

    q = [] 
    heapq.heappush(q,(0,start))

    while q:
        d,curr = heapq.heappop(q)

        if curr==end:
            return distance[end]

        for i in graph[curr]:
            x = d + i[1]
            if x < distance[i[0]]:
                distance[i[0]] = x
                heapq.heappush(q,(x,i[0]))
    
    return inf
# 1 -> v1 -> v2 -> n / 1 -> v2 -> v1 -> n      두가지 경로 중 작은 값이 정답
inf = int(10**9)
route_v1v2 = dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
route_v2v1 = dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)
if route_v1v2 >= inf and route_v2v1 >= inf:
    print(-1)
else:
    print(min(route_v1v2,route_v2v1))