# 미확인 도착지

import heapq
import sys
input = sys.stdin.readline

#데이크스트라 알고리즘
def dijkstra(start,end):

    distance = [inf]*(n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q,(0,start))

    while q:
        d,curr = heapq.heappop(q)

        if curr == end:
            return distance[end]
        
        for i in graph[curr]:
            x = d + i[1]
            if x < distance[i[0]]:
                distance[i[0]] = x
                heapq.heappush(q,(x,i[0]))

    return inf

inf = int(10**9)
T = int(input())
for _ in range(T):
    n,m,t = map(int,input().split())    # 교차로, 도로, 목적지 후보의개수
    s,g,h = map(int,input().split())    # 출발지, g와 h 사이에 흔적이있다
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split()) # a,b사이의 도로의 길이 : d
        graph[a].append([b,d])
        graph[b].append([a,d])
    
    dest = [] # 목적지 후보
    for _ in range(t):
        k = int(input())

        # 우회로 두가지중 짧은거리
        detour = min(dijkstra(s,g) + dijkstra(g,h) + dijkstra(h,k),
                     dijkstra(s,h) + dijkstra(h,g) + dijkstra(g,k))
        # 최단거리
        route = dijkstra(s,k) 
        if detour == route:     # 우회한 길이 더 길면 불가능이다
            dest.append(k)

    dest.sort()
    for x in dest:  
        print(x,end=' ')
    print()