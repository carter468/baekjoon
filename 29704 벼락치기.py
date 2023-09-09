# 벼락치기
# Gold 5, knapsack, dp

import sys
input = sys.stdin.readline

n,t = map(int,input().split())
hw = [(0,0)]+[tuple(map(int,input().split())) for _ in range(n)]

dp = [[0]*(t+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,t+1):
        cost = hw[i][0]
        value = hw[i][1]
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-cost]+value)

print(sum([hw[i][1] for i in range(n+1)])-dp[n][t])