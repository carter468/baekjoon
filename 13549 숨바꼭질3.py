# 숨바꼭질3

import heapq

n,k = map(int,input().split())

# 데이크스트라 알고리즘
def dijkstra(start,end):
    # if start >= end:
    #     return start-end
    q = []
    heapq.heappush(q,(0,start))     # 현재거리:0, 위치:start
    inf = int(10**9)
    distance = [inf]*100001
    distance[start] = 0

    while q:
        dist, loca = heapq.heappop(q)

        if loca == end:
            return distance[end]

        x = loca + 1
        d = dist + 1
        if x < 100001 and d < distance[x]:
            distance[x] = d
            heapq.heappush(q,(d,x))

        x = loca - 1
        d = dist + 1
        if 0 <= x < 100001 and d < distance[x]:
            distance[x] = d
            heapq.heappush(q,(d,x))

        x = loca * 2
        d = dist
        if x < 100001 and d < distance[x]:
                distance[x] = d
                heapq.heappush(q,(d,x))
   
print(dijkstra(n,k))