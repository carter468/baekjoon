# Cow Hurdles
# Gold 4, Floyd-Warshall

import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m,t = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s,e,h = map(int,input().split())
    graph[s][e] = h

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],max(graph[i][k],graph[k][j]))

for _ in range(t):
    a,b = map(int,input().split())
    print(graph[a][b] if graph[a][b] != INF else -1)