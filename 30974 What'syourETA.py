# What's your ETA?
# Gold 4, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize
M = 10**7+1

seive = [True]*M
for i in range(2,int(M**0.5)+1):
    if seive[i] == True:
        for j in range(i*i,M,i):
            seive[j] = False

n,m = map(int,input().split())
arr = [0]+list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    if seive[arr[u]+arr[v]] == True:
        graph[u].append((w,v))
        graph[v].append((w,u))

distance = [INF]*(n+1)
distance[1] = 0
q = [(0,1)]
while q:
    d,x = heapq.heappop(q)
    if d > distance[x]: continue
    for dd,nx in graph[x]:
        nd = d+dd
        if nd < distance[nx]:
            distance[nx] = nd
            heapq.heappush(q,(nd,nx))

print(distance[n] if distance[n] != INF else 'Now where are you?')