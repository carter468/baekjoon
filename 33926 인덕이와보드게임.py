# 인덕이와 보드게임
# Gold 5, DP

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
B = [tuple(map(int,input().split())) for _ in range(N)]
C = [tuple(map(int,input().split())) for _ in range(N)]

dp = [[[-10**9,10**9] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if (i,j) == (0,0):
            dp[i][j] = [B[0][0],B[0][0]]
        elif i == 0:
            a,b = dp[i][j-1]
            if C[i][j] == 0:
                dp[i][j] = [a+B[i][j],b+B[i][j]]
            else:
                dp[i][j] = [-b-B[i][j],-a-B[i][j]]
        elif j == 0:
            a,b = dp[i-1][j]
            if C[i][j] == 0:
                dp[i][j] = [a+B[i][j],b+B[i][j]]
            else:
                dp[i][j] = [-b-B[i][j],-a-B[i][j]]
        else:
            a = max(dp[i-1][j][0],dp[i][j-1][0])
            b = min(dp[i-1][j][1],dp[i][j-1][1])
            if C[i][j] == 0:
                dp[i][j] = [a+B[i][j],b+B[i][j]]
            else:
                dp[i][j] = [-b-B[i][j],-a-B[i][j]]

print(dp[-1][-1][0])