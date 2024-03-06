# 양갈래 구하기
# Gold 3, DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node,t):
    visited[node] = True
    k = 0
    for x,v in graph[node]:
        if not visited[x]:
            k += dfs(x,v)
    if k == 0: k = sys.maxsize
    return min(k,t)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,v = map(int,input().split())
    graph[a].append((b,v))
    graph[b].append((a,v))
visited = [False]*(n+1)
print(dfs(1,sys.maxsize))