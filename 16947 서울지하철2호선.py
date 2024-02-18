# 서울 지하철 2호선
# Gold 3, DFS

import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
temp = [[] for _ in range(n+1)]
for _ in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    temp[a].append(b)
    temp[b].append(a)

arr = []
for i in range(1,n+1):
    if len(temp[i]) == 1: arr.append(i)
dist = [0]*(n+1)
while arr:
    narr = []
    for i in arr:
        dist[i] = -1
        j = temp[i].pop()
        temp[j].remove(i)
        if len(temp[j]) == 1: narr.append(j)
    arr = narr

q = []
for i in range(1,n+1):
    if dist[i] == 0: q.append(i)
while q:
    x = q.pop()
    for nx in graph[x]:
        if dist[nx] == -1:
            dist[nx] = dist[x]+1
            q.append(nx)
print(*dist[1:])