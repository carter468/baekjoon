# Dragon Ball I
# Gold 2, dijkstra, bruteforcing

import heapq,itertools

def dijkstra(start):
    dist = [1<<99]*(N+1)
    dist[start] = 0
    q = [(0,start)]
    while q:
        d,x = heapq.heappop(q)
        if d > dist[x]: continue
        for nx,dd in graph[x]:
            nd = d+dd
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(q,(nd,nx))
    return dist

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))
ball = tuple(set(map(int,input().split())))

l = len(ball)
dist_dict = dict()
for x in ball:
    dist_dict[x] = dijkstra(x)
dist_dict[1] = dijkstra(1)

result = 1<<99
for p in itertools.permutations(range(l)):
    x = 0
    s = 1
    for i in range(l):
        e = ball[p[i]]
        x += dist_dict[s][e]
        s = e
    result = min(result,x)
print(result if result < 1<<99 else -1)