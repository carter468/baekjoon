# 도시 분할 계획
# Gold 4, MST

import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

result = []
visited = [False]*(n+1)
q = [(0,1)]
while q:
    d,x = heapq.heappop(q)
    if visited[x]: continue
    visited[x] = True
    result.append(d)
    if len(result) == n: break
    for nx,nd in graph[x]:
        heapq.heappush(q,(nd,nx))
print(sum(result)-max(result))