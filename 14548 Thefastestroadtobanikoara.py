# The fastest road to banikoara
# Gold 4, dijkstra

from collections import defaultdict
import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

for _ in range(int(input())):
    n,dep,des = input().split()
    dist = defaultdict(list)
    result = {}
    for _ in range(int(n)):
        a,b,c = input().split()
        dist[a].append((b,int(c)))
        dist[b].append((a,int(c)))
        result[a] = INF
        result[b] = INF

    q = [(0,dep)]
    result[dep] = 0
    while q:
        d,x = heapq.heappop(q)
        if result[x] < d: continue
        for nx,nd in dist[x]:
            nd += d
            if nd < result[nx]:
                result[nx] = nd
                heapq.heappush(q,(nd,nx))

    print(dep,des,result[des])