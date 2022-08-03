# 최소비용구하기2

import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        cost,curr = heapq.heappop(q)  # 비용, 도시
        if distance[curr] < cost:     # 이미 탐색된 상황
            continue
        for x in graph[curr]:
            cost1 = cost+x[1]         
            if cost1 < distance[x[0]]:
                distance[x[0]] = cost1
                heapq.heappush(q,(cost1,x[0]))
                p[x[0]] = curr

n = int(input())    # 도시의 개수
m = int(input())    # 버스의 개수
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())    #출발,도착,비용
    graph[a].append([b,c])              #(도착,비용)
start,end = map(int,input().split())

INF = int(1e9)
distance = [INF]*(n+1)
p = [start]*(n+1)

dijkstra(start)
ans = []
temp = end
while temp != start:
    ans.append(temp)
    temp = p[temp]
ans.append(start)

print(distance[end])
print(len(ans))
print(*reversed(ans))