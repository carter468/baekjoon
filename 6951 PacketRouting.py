# Packet Routing
# Gold 5, floyd-warshall

import sys
input = sys.stdin.readline

n,w,p = map(int,input().split())
graph = [[50000]*(n+1) for _ in range(n+1)]
for _ in range(w):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for _ in range(p):
    a,b = map(int,input().split())
    print(graph[a][b])