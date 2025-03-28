# 택배
# Gold 3, floyd-warshall

import sys
input = sys.stdin.readline
INF = 10**9

N,M = map(int,input().split())
dist = [[(INF,'-') for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    u,v,d = map(int,input().split())
    if d < dist[u][v][0]: dist[u][v] = (d,v)
    if d < dist[v][u][0]: dist[v][u] = (d,u)

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j: continue
            d = dist[i][k][0]+dist[k][j][0]
            if d < dist[i][j][0]: dist[i][j] = (d,dist[i][k][1])

for i in range(1,N+1):
    for j in range(1,N+1):
        print(dist[i][j][1],end=' ')
    print()