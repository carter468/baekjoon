# Hoof, Paper, Scissors (Gold)
# Gold 3, DP

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dp = [[[0,0,0] for _ in range(k+1)] for _ in range(n+1)]
for i in range(1,n+1):
    g = input().strip()
    if g == 'H': g = 0
    elif g == 'P': g = 1
    elif g == 'S': g = 2
    for j in range(k+1):
        if j == 0:
            dp[i][j][g] = dp[i-1][j][g]+1
            dp[i][j][g-1] = dp[i-1][j][g-1]
            dp[i][j][g-2] = dp[i-1][j][g-2]
        else:
            dp[i][j][g] = max(dp[i-1][j][g],dp[i-1][j-1][g-1],dp[i-1][j-1][g-2])+1
            dp[i][j][g-1] = max(dp[i-1][j-1][g],dp[i-1][j][g-1],dp[i-1][j-1][g-2])
            dp[i][j][g-2] = max(dp[i-1][j-1][g],dp[i-1][j-1][g-1],dp[i-1][j][g-2])

result = 0
for i in range(k+1):
    result = max(result,max(dp[-1][i]))
print(result)