# 떡 돌리기
# Gold 4, dijkstra

import sys,heapq
input = sys.stdin.readline

N,M,X,Y = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
dist = [10**9]*N
dist[Y] = 0
q = [(0,Y)]
while q:
    d,x = heapq.heappop(q)
    if dist[x] < d: continue
    for dd,nx in graph[x]:
        nd = d+dd*2
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(q,(nd,nx))
count = 1
t = 0
for d in sorted(dist):
    if d > X:
        print(-1)
        break
    if t+d <= X:
        t += d
    else:
        count += 1
        t = d
else: print(count)