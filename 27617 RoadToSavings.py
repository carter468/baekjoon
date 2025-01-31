# Road To Savings
# Gold 4, dijkstra

import heapq

n,m,a,b = map(int,input().split())
graph = [[] for _ in range(n+1)]
total = 0
for _ in range(m):
    i,j,l = map(int,input().split())
    graph[i].append((j,l))
    graph[j].append((i,l))
    total += l

dist = [1<<14]*(n+1)
dist[a] = 0
q = [(0,a)]
while q:
    d,x = heapq.heappop(q)
    if d > dist[x]: continue
    for nx,l in graph[x]:
        nd = d+l
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(q,(nd,nx))

visited = set()
q = [(dist[b],b)]
while q:
    d,x = q.pop()
    for nx,l in graph[x]:
        if d-l == dist[nx] and (x,nx,l) not in visited:
            visited.add((x,nx,l))
            q.append((d-l,nx))

for x,nx,l in visited:
    total -= l
print(total)