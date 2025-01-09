# Minimum Spanning Arborescence
# Gold 2, greedy, DAG

import sys
input = sys.stdin.readline
INF = sys.maxsize

N,M,r = map(int,input().split())
min_w = [INF]*(N+1)
for _ in range(M):
    u,v,c = map(int,input().split())
    min_w[v] = min(min_w[v],c)

result = 0
for i in range(1,N+1):
    if i != r:
        if min_w[i] == INF:
            print(-1)
            break
        result += min_w[i]
else: print(result)   