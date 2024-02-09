# MST 게임
# Gold 3, MST

import sys,heapq
input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append((i+1,y))
    graph[y].append((i+1,x))

for i in range(k):
    visited = [False]*(n+1)
    result = 0
    count = 0
    q = [(0,1)]
    while q:
        d,x = heapq.heappop(q)
        if visited[x]: continue
        visited[x] = True
        result += d
        count += 1
        for nd,nx in graph[x]:
            if nd > i: heapq.heappush(q,(nd,nx))
    if count != n: result = 0
    print(result,end=' ')