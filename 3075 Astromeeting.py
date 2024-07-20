# Astromeeting
# Gold 3, floyd-warshall

import sys
input = sys.stdin.readline
INF = sys.maxsize

for _ in range(int(input())):
    n,p,q = map(int,input().split())
    arr = [int(input()) for _ in range(n)]
    dist = [[INF]*(p+1) for _ in range(p+1)]
    for _ in range(q):
        i,j,d = map(int,input().split())
        dist[i][j] = min(dist[i][j],d)
        dist[j][i] = min(dist[j][i],d)

    for k in range(1,p+1):
        dist[k][k] = 0
        for i in range(1,p+1):
            for j in range(1,p+1):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    
    result = [0,INF]
    for i in range(1,p+1):
        cost = 0
        for j in arr:
            if dist[i][j] == INF:
                cost = INF
                break
            cost += dist[i][j]**2
        if cost < result[1]: result = [i,cost]
    print(*result)