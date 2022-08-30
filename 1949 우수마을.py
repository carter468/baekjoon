# 우수마을

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x):
    visited[x] = 1
    for i in tree[x]:
        if not visited[i]:
            dfs(i)
            dp[x][1] += dp[i][0]        # 현재마을을 우수마을로
            dp[x][0] += max(dp[i][0],dp[i][1])  #현재마을을 일반마을로

n = int(input())
cost = [0] + list(map(int,input().split()))
tree = [[] for _ in range(n+1)]
dp = [[0,cost[i]]*2 for i in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
print(max(dp[1][1],dp[1][0]))