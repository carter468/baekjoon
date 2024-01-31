# 인하니카 공화국
# Gold 3, DFS, tree dp

import sys
input = sys.stdin.readline

def dfs(node):
    for ne,d in graph[node]:
        if not visited[ne]:
            visited[ne] = True
            dp[node] += min(d,dfs(ne))
    return dp[node] if dp[node] else 10**9

for _ in range(int(input())):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    
    dp = [0]*(n+1)
    visited = [False]*(n+1)
    visited[1] = True
    dfs(1)
    print(dp[1])