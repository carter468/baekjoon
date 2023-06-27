# 로또
# Gold 4, DP

import sys
input = sys.stdin.readline
M = 2001

dp = [[0]*M for _ in range(10)]
dp[0] = [1]*M
for i in range(1,10):
    for j in range(2**i,M):
        dp[i][j] = sum(dp[i-1][1:j//2+1])

for _ in range(int(input())):
    n,m = map(int,input().split())
    print(sum(dp[n-1][1:m+1]))