# 게임을 클리어하자
# Gold 5, DP

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
dp[0] = arr[0]
for i in range(1,n):
    for j in range(m):
        t = sys.maxsize
        for k in range(m):
            if j == k: continue
            t = min(t,dp[i-1][k])
        dp[i][j] = arr[i][j]+t

print(min(dp[-1]))