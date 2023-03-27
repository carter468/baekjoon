# 인터넷 설치
# Gold 1, dijkstra, 이분 탐색

import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(t):
    q = []
    distance = [INF]*(n+1)
    heapq.heappush(q,(0,1))
    distance[1] = 0
    while q:
        dist,node = heapq.heappop(q)
        if distance[node] < dist: continue
        for x in graph[node]:
            if x[0] > t:
                if dist+1 < distance[x[1]]:
                    distance[x[1]] = dist+1
                    heapq.heappush(q,(dist+1,x[1]))
            else:
                if dist < distance[x[1]]:
                    distance[x[1]] = dist
                    heapq.heappush(q,(dist,x[1]))
    
    return distance[n] <= k

n,p,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(p):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

left,right = 0,1000001
answer = INF
while left <= right:
    mid = (left+right)//2
    if dijkstra(mid):
        right = mid-1
        answer = mid
    else:
        left = mid+1

print(answer if answer != INF else -1)