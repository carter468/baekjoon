# 정상 회담 2
# Gold 3, DP

n = int(input())//2

dp = [0]*(n+1)
dp[0],dp[1] = 1,1
for i in range(2,n+1):
    for j in range(i):
        dp[i] += dp[j]*dp[i-1-j]%987654321
    dp[i] %= 987654321

print(dp[n])