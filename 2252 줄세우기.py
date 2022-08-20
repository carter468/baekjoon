# 줄 세우기

from collections import deque
import sys
input = sys.stdin.readline

def topologysort():
    result = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()
        result.append(x)
        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    print(*result)
    
n,m = map(int,input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    indegree[b] += 1
    graph[a].append(b)
topologysort()