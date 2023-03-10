# 벼락치기
# Gold 5, dp

import sys
input = sys.stdin.readline

n,t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*(t+1) for _ in range(n+1)]
for i in range(1,n+1):
    for w in range(1,t+1):
        if arr[i-1][0]<=w:
            dp[i][w] = max(arr[i-1][1]+dp[i-1][w-arr[i-1][0]],dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][t])