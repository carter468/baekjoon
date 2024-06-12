# 농부 비니
# Gold 3, DP

import sys
input = sys.stdin.readline

M = 10**9+7
N = 10001

dp = [[[0]*2 for _ in range(7)] for _ in range(N)]
for i in range(1,10):
    if i == 7: dp[1][0][1] += 1
    else: dp[1][i%7][0] += 1
for i in range(2,N):
    for j in range(7): 
        for k in range(10): 
            x = (j+k)%7
            if k in (0,7):
                dp[i][x][1] = (dp[i][x][1]+sum(dp[i-1][j]))%M
            else:
                dp[i][x][0] = (dp[i][x][0]+dp[i-1][j][0])%M
                dp[i][x][1] = (dp[i][x][1]+dp[i-1][j][1])%M

for _ in range(int(input())):
    print(dp[int(input())][0][1])