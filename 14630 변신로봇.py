# 변신로봇
# Gold 3, 데이크스트라

import sys
import heapq
input = sys.stdin.readline

def dijkstra(start,end):
    INF = int(1e9)
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in range(1,n+1):
            x = dist+cost[i][node]
            if x<distance[i]:
                distance[i] = x
                heapq.heappush(q,(x,i))
    return distance[end]

def get_cost(i,j):
    total = 0
    for k in range(l):
        total += (int(robot[i][k])-int(robot[j][k]))**2
    return total

robot = ['']
n = int(input())
for _ in range(n):
    robot.append(input().strip())
l = len(robot[-1])

cost = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(i+1,n+1):
        cost[i][j] = get_cost(i,j)
        cost[j][i] = cost[i][j]

a,b = map(int,input().split())
print(dijkstra(a,b))