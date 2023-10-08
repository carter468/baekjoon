# Moocast
# Gold 3, MST(Prim)

import heapq

n = int(input())
cows = [tuple(map(int,input().split())) for _ in range(n)]

edge = [(0,0)]
visit = [0]*n
result = 0
while edge:
    dist,node = heapq.heappop(edge)
    if not visit[node]: 
        result = max(result,dist)
        visit[node] = 1
        for i in range(n):
            if not visit[i]:
                d = (cows[i][0]-cows[node][0])**2+(cows[i][1]-cows[node][1])**2
                heapq.heappush(edge,(d,i))
print(result)