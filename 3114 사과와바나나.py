# 사과와 바나나
# Gold 2, DP, prefix sum

import sys
input = sys.stdin.readline

R,C = map(int,input().split())
A = [input().split() for _ in range(R)]

ap = [[0]*(C+1) for _ in range(R)]
ba = [[0]*(C+1) for _ in range(R)]
for i in range(R):
    for j in range(C):
        c = int(A[i][j][1:])
        if A[i][j][0] == 'A': a,b = c,0
        else: a,b = 0,c
        ap[i][j+1] += ap[i][j]+a
        ba[i][j+1] += ba[i][j]+b

dp = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if j == 0:
            dp[i][j] = dp[i-1][j]+ba[i][C]-ba[i][j+1]
        elif i == 0:
            dp[i][j] = dp[i][j-1]+ba[i][j]-ba[i][j+1]
        else:
            dp[i][j] = max(max(dp[i-1][j-1],dp[i-1][j])+ba[i][C]-ba[i][j+1]+ap[i][j],dp[i][j-1]+ba[i][j]-ba[i][j+1])
print(dp[-1][-1])