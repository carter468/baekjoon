# 골목길
# Gold 1, Bellman-Ford

import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
edge = [tuple(map(int,input().split())) for _ in range(m)]

# BellmanFord
distance = [-INF]*(n+1)
distance[1] = 0
parent = [0]*(n+1)
for i in range(n):
    for a,b,c in edge:
        if distance[a] != -INF and distance[a]+c > distance[b]:
            distance[b] = distance[a]+c
            parent[b] = a
            if i == n-1:
                distance[b] = INF

if distance[n] == INF: print(-1)
else:
    result = [n]
    i = n
    while i != 1:
        if i == parent[i]:
            print(-1)
            break
        i = parent[i]
        result.append(i)
    else: print(*result[::-1])