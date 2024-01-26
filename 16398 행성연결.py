# 행성 연결
# Gold 4, MST

import heapq

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

result = 0
visited = [False]*n
q = [(0,0)]
while q:
    cost,node = heapq.heappop(q)
    if visited[node]: continue
    visited[node] = True
    result += cost
    for i in range(n):
        if node != i: heapq.heappush(q,(arr[i][node],i))
print(result)