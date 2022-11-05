# 플로이드2

import sys
input = sys.stdin.readline
INF = sys.maxsize

def find_path(i,j):
    if trace[i][j] == 0:
        return []
    k = trace[i][j]
    return find_path(i,k)+[k]+find_path(k,j)

n = int(input())   
distance = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    distance[i][i] = 0
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    distance[a][b] = min(distance[a][b],c)

trace = [[0]*(n+1) for _ in range(n+1)]
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                trace[i][j] = k
for i in range(1,n+1):
    for j in range(1,n+1):
        print(distance[i][j] if distance[i][j]!=INF else 0,end=' ')
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j]==0 or distance[i][j]==INF:
            print(0)
            continue
        path = [i]+find_path(i,j)+[j]
        print(len(path),*path)