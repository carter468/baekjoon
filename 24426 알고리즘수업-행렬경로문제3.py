# 알고리즘 수업 - 행렬 경로 문제 3
# Gold 4, DP

import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]
R,C = map(int,input().split())

dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,R+1):
    for j in range(1,C+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])+arr[i-1][j-1]
for i in range(R,N+1):
    for j in range(C,N+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])+arr[i-1][j-1]
print(dp[N][N],end=' ')

dp = [[-10**9]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if (i,j) == (1,1): dp[1][1] = arr[0][0]
        elif (i-1,j) == (R,C): dp[i][j] = dp[i][j-1]+arr[i-1][j-1]
        elif (i,j-1) == (R,C): dp[i][j] = dp[i-1][j]+arr[i-1][j-1]
        else: dp[i][j] = max(dp[i-1][j],dp[i][j-1])+arr[i-1][j-1]
print(dp[N][N])