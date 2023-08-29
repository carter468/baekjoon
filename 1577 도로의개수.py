# 도로의 개수
# Gold 5, DP

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = set()
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    arr.add((a,b,c,d))
    arr.add((c,d,a,b))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n+1):
    for j in range(m+1):
        if (i,j,i-1,j) not in arr:
            dp[i][j] += dp[i-1][j]
        if (i,j,i,j-1) not in arr:
            dp[i][j] += dp[i][j-1]
print(dp[n][m])