# 암호
# Gold 1, DP

n,k = map(int,input().split())

dp = [1]+[0]*n
for i in range(1,n+1):
    dp[i] = (dp[i-1]*k - dp[i-5]*2 + dp[i-7]) % (10**9+9)

print(dp[n])