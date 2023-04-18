# Ezreal 여눈부터 가네 ㅈㅈ
# Gold 5, DP

MOD = 10**9+7

n = int(input())

dp = [[0]*3 for _ in range(1516)]
dp[2][0],dp[2][1] = 1,1
for i in range(3,n+1):
    for j in range(3):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j-2])%MOD

print(dp[n][0])