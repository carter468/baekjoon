# 노드 사이의 거리

import heapq

n,m = map(int,input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,d = map(int,input().split())
    tree[a].append([b,d])
    tree[b].append([a,d])

def dijkstra(start,end): 
    distance = [inf]*(n+1)
    distance[start] = 0
    q = [(0,start)] 
    while q:
        d,curr = heapq.heappop(q)
        if curr == end:
            return distance[end]
        for i in tree[curr]:
            x = d + i[1]
            if x < distance[i[0]]:
                distance[i[0]] = x
                heapq.heappush(q,(x,i[0]))

inf = int(10**9)
for _ in range(m):
    a,b = map(int,input().split())
    print(dijkstra(a,b))