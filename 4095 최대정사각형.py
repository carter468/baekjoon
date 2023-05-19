# 최대 정사각형
# Gold 4, DP

import sys
input = sys.stdin.readline

while 1:
    n,m = map(int,input().split())
    if n == 0: break
    matrix = [tuple(input().split()) for _ in range(n)]
    
    dp = [[0]*m for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
            result = max(result,dp[i][j])
    print(result)