# Conquest
# Gold 5, greedy, priority queue

import sys,heapq
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
arr = [0]+[int(input()) for _ in range(N)]

result = arr[1]
q = []
visited = {1}
for nx in graph[1]:
    if nx not in visited:
        visited.add(nx)
        heapq.heappush(q,(arr[nx],nx))
while q and result > q[0][0]:
    c,x = heapq.heappop(q)
    result += c
    for nx in graph[x]:
        if nx not in visited:
            visited.add(nx)
            heapq.heappush(q,(arr[nx],nx))
print(result)