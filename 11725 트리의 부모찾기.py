# 트리의 부모찾기

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0]*(n+1)
q = deque()
q.append(1)
while q:
    x = q.popleft()
    for i in graph[x]:
        if parent[i] == 0:
            parent[i] = x
            q.append(i)

for i in range(2,n+1):
    print(parent[i])