# 가희와 터널
# Gold 2, DP

M = 998244353

s = int(input())

dp = [[0]*8 for _ in range(s+1)]
dp[0][0] = 1
for i in range(1,s+1):
    for j in range(8):
        if j == 0:
            dp[i][j] = dp[i-1][j]*6%M
        elif j == 7:
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j]*7)%M
        else:
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j]*6)%M

print(dp[-1][-1])