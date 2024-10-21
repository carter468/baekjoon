# 알고리즘 수업 - 행렬 경로 문제 6
# Gold 4, DP

import sys
input = sys.stdin.readline
    
n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]
m = int(input())
p = sorted([(n,n)]+[tuple(map(int,input().split())) for _ in range(m)])

dp = [[0]*(n+1) for _ in range(n+1)]
dp[1][1] = arr[0][0]
x,y = 1,1
for xx,yy in p:
    if y > yy:
        dp[n][n] = -1
        break
    for i in range(x,xx+1):
        for j in range(y,yy+1):
            if i > x and j > y:
                dp[i][j] = arr[i-1][j-1]+max(dp[i-1][j],dp[i][j-1])
            elif i > x:
                dp[i][j] = arr[i-1][j-1]+dp[i-1][j]
            elif j > y:
                dp[i][j] = arr[i-1][j-1]+dp[i][j-1]
    x,y = xx,yy
print(dp[n][n])