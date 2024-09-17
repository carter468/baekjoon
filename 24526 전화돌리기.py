# 전화 돌리기
# Gold 2, DFS, DP

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x):
    if dp[x] != -1: return dp[x]
    if visited[x]: return 0
    visited[x] = True
    result = 1
    for nx in graph[x]:
        if dfs(nx) != 1:
            result = 0
            break
    visited[x] = False
    dp[x] = result
    return dp[x]

n,m = map(int,input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].add(b)

count = 0
dp = [-1]*(n+1)
visited = [False]*(n+1)
for i in range(1,n+1):
    if dfs(i) == 1: count += 1
print(count)