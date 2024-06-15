# 모비스터디
# Gold 3, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = 10**15

n,m,s,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

dist = [INF]*(n+1)
dist[s] = 0
q = [(0,s)]
while q:
    d,x = heapq.heappop(q)
    if d > dist[x]: continue
    for dd,nx in graph[x]:
        nd = d+dd
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(q,(nd,nx))

result = {e}
q = [e]
while q:
    x = q.pop()
    for d,nx in graph[x]:
        if dist[nx]+d == dist[x] and nx not in result:
            result.add(nx)
            q.append(nx)
            
print(len(result))
print(*sorted(result))