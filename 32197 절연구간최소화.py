# 절연 구간 최소화
# Gold 4, dijkstra

import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a].append((t,b))
    graph[b].append((t,a))
s,e = map(int,input().split())

dist = [[10**9]*2 for _ in range(n+1)]
dist[s] = [0,0]
q = []
for nt,nx in graph[s]:
    q.append((0,nx,nt))
    dist[nx][nt] = 0
while q:
    d,x,t = heapq.heappop(q)
    if d > dist[x][t]: continue
    for nt,nx in graph[x]:
        if t == nt:
            if d < dist[nx][t]:
                dist[nx][t] = d
                heapq.heappush(q,(d,nx,t))
        else:
            if d+1 < dist[nx][nt]:
                dist[nx][nt] = d+1
                heapq.heappush(q,(d+1,nx,nt))
print(min(dist[e]))
