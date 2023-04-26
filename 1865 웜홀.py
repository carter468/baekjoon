# 웜홀
# Gold 3, 벨만포드

import sys
input = sys.stdin.readline
INF = sys.maxsize

def bellmanford():
    n,m,w = map(int,input().split())
    edge = []
    for _ in range(m):
        a,b,c = map(int,input().split())
        edge.append((a,b,c))
        edge.append((b,a,c))
    for _ in range(w):
        a,b,c = map(int,input().split())
        edge.append((a,b,-c))
    distance = [INF]*(n+1)
    distance[1] = 0

    for i in range(n):
        for a,b,c in edge:
            if distance[b] > distance[a]+c:
                distance[b] = distance[a]+c
                if i == n-1:
                    return 'YES'
    return 'NO'

for _ in range(int(input())):
    print(bellmanford())