# ACM Craft
# Gold 3, DP, topological sort

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,k = map(int,input().split())
    d = tuple(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    for _ in range(k):
        x,y = map(int,input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())

    result = [0]*(n+1)
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = d[i-1]
    while q:
        x = q.popleft()
        if x == w:
            print(result[x])
            break
        for nx in graph[x]:
            result[nx] = max(result[nx],result[x]+d[nx-1])
            indegree[nx] -= 1
            if indegree[nx] == 0:
                q.append(nx)