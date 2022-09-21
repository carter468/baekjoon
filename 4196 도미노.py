# 도미노

import sys
from xml.dom import INDEX_SIZE_ERR
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)
    stack.append(x)

def dfs_r(x):
    visited[x] = 1
    ids[x] = idx
    stack.append(x)
    for i in graph_r[x]:
        if visited[i] == 0:
            dfs_r(i)

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    graph_r = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph_r[b].append(a)

    stack = []
    visited = [0] *(n+1)
    for i in range(1,n+1):
        if visited[i] == 0:
            dfs(i)

    ids = [-1]*(n+1)
    idx = 0
    result = []
    visited = [0] *(n+1)
    while stack:
        scc = []
        x = stack.pop()
        if visited[x] == 0:
            idx += 1
            dfs_r(x)
            result.append(sorted(scc))
    indegree = [0]*(idx+1)

    for i in range(1,n+1):
        for x in graph[i]:
            if ids[i] != ids[x]:
                indegree[ids[x]] += 1
    cnt = 0
    for i in range(1,len(indegree)):
        if indegree[i] == 0:
            cnt += 1
    print(cnt)
    