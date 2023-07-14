# 알약
# Gold 5, DP

import sys

dp = [[0]*31 for _ in range(31)]
for i in range(31):
    for j in range(31):
        if i<j: continue
        if j==0: dp[i][j] = 1
        else: dp[i][j] = dp[i-1][j]+dp[i][j-1]

while n:=int(sys.stdin.readline()):
    print(dp[n][n])