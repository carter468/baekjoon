# Rainbow Road Race
# Gold 1, dijkstra, bitmask

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize
dic = {'R':0,'O':1,'Y':2,'G':3,'B':4,'I':5,'V':6}

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,d,c = input().split()
    u,v,d = map(int,(u,v,d))
    c = dic[c]
    graph[u].append((v,d,c))
    graph[v].append((u,d,c))

dist = [[INF]*(128) for _ in range(N+1)]
dist[1][0] = 0
q = [(0,1,0)]
result = INF
while q:
    d,x,v = heapq.heappop(q)
    if d > dist[x][v]: continue
    for nx,dd,c in graph[x]:
        nd = d+dd
        nv = v|(1<<c)
        if nd < dist[nx][nv]:
            dist[nx][nv] = nd
            heapq.heappush(q,(nd,nx,nv))
print(dist[1][127])