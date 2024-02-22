# Game Map
# Gold 4, DFS, DP

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    if dp[node]: return dp[node]
    c = 1
    for nx in graph[node]:
        if count[nx] > count[node]:
            c = max(c,dfs(nx)+1)
    dp[node] = c
    return dp[node]

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
count = [0]*n
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    count[a] += 1
    count[b] += 1

dp = [0]*n
for i in range(n):
    dfs(i)
print(max(dp))