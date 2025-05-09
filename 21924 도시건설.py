# 도시 건설
# Gold 4, MST

import sys,heapq
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
result = 0
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    result += c

visited = [False]*(N+1)
q = [(0,1)]
while q:
    c,x = heapq.heappop(q)
    if visited[x]: continue
    visited[x] = True
    result -= c
    for nc,nx in graph[x]:
        heapq.heappush(q,(nc,nx))
        
print(result if all(visited[1:]) else -1)