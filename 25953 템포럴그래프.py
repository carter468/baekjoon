# 템포럴 그래프
# Gold 3, DP

import sys
input = sys.stdin.readline
INF = sys.maxsize

N,T,M = map(int,input().split())
S,E = map(int,input().split())
dist = [INF]*N
dist[S] = 0
for _ in range(T):
    update = set()
    for _ in range(M):
        u,v,w = map(int,input().split())
        if v not in update and dist[u] > dist[v]+w:
            dist[u] = min(dist[u],dist[v]+w)
            update.add(u)
        if u not in update and dist[v] > dist[u]+w:
            dist[v] = min(dist[v],dist[u]+w)
            update.add(v)

print(dist[E] if dist[E] < INF else -1)