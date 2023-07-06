# 장난감 조립
# Gold 2, DP, 위상정렬

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
count = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1)

for _ in range(int(input())):
    x,y,k = map(int,input().split())
    graph[y].append((x,k))
    degree[x] += 1

q = deque()
for i in range(1,n+1):
    if degree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    for x,y in graph[now]:
        if sum(count[now]) == 0:
            count[x][now] += y
        else:
            for i in range(1,n+1):
                count[x][i] += count[now][i]*y
        degree[x] -= 1
        if degree[x] == 0:
            q.append(x)

for i,x in enumerate(count[n]):
    if x: print(i,x)