# 복권 표
# Gold 1, DP

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M,Z,R = map(int,input().split())
    
    M = str(M-1)
    N = len(M)
    Z = str(Z).zfill(N)

    dp = [[[0]*R for _ in range(2)] for _ in range(N)]

    if M[0] == Z[0]:
        dp[0][0][0] = int(M[0])
        if R > 1: dp[0][1][1] = 1
    else:
        dp[0][0][0] = int(M[0])-1
        dp[0][1][0] = 1
        if R > 1: dp[0][0][1] = 1

    for i in range(N-1):
        z = int(Z[i+1])
        m = int(M[i+1])
        for j in range(R):
            if m > z:
                dp[i+1][0][0] += dp[i][1][j]*(m-1)
                if j < R-1:
                    dp[i+1][0][j+1] += dp[i][1][j]
                dp[i+1][1][0] += dp[i][1][j]
            elif m == z:
                dp[i+1][0][0] += dp[i][1][j]*m
                if j < R-1:
                    dp[i+1][1][j+1] += dp[i][1][j]
            else:
                dp[i+1][0][0] += dp[i][1][j]*m
                dp[i+1][1][0] += dp[i][1][j]

            dp[i+1][0][0] += dp[i][0][j]*9
            if j < R-1:
                dp[i+1][0][j+1] += dp[i][0][j]

    print(int(M)+1-sum(dp[-1][0])-sum(dp[-1][1]))