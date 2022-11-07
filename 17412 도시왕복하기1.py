# 도시 왕복하기

import sys
input = sys.stdin.readline
from collections import deque

INF = sys.maxsize
MAX = 401
capacity = [[0 for _ in range(MAX)] for _ in range(MAX)]
flow = [[0 for _ in range(MAX)] for _ in range(MAX)]

n,p = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(p):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    capacity[a][b] = 1

def find_max_flow(start,end):
    answer = 0
    while True:
        path = [-1]*(n+1)
        q = deque([start])
        while q:
            x = q.popleft()
            for i in range(len(graph[x])):
                y = graph[x][i]
                if capacity[x][y]-flow[x][y]>0 and path[y] == -1:
                    path[y] = x
                    q.append(y)
                    if y==end:
                        break
        if path[end] == -1:
            break
        f = INF
        i = end
        while i!=start:
            f = min(f,capacity[path[i]][i]-flow[path[i]][i])
            i = path[i]
        i = end
        while i!=start:
            flow[path[i]][i] += f
            flow[i][path[i]] -= f
            i = path[i]
        answer += f
    return answer

print(find_max_flow(1,2))