# 디저트

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
satisfaction_dessert = []
for _ in range(m):
    satisfaction_dessert.append(list(map(int,input().split())))

dp = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
    dp[0][i] = satisfaction_dessert[i][0]
for i in range(1,n):
    for j in range(m):
        for k in range(m):
            if j==k:
                dp[i][j] = max(dp[i][j],dp[i-1][k] + satisfaction_dessert[j][i]//2)
            else:
                dp[i][j] = max(dp[i][j],dp[i-1][k] + satisfaction_dessert[j][i])
print(max(dp[-1]))