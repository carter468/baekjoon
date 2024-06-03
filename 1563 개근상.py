# 개근상
# Gold 4, DP

M = 10**6

n = int(input())

dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)] 
dp[0][0][0] = 1

for i in range(1,n+1):
    dp[i][0][0] = sum(dp[i-1][0])%M  
    dp[i][1][0] = (sum(dp[i-1][0])+sum(dp[i-1][1]))%M 
    dp[i][0][1] = dp[i-1][0][0] 
    dp[i][1][1] = dp[i-1][1][0]
    dp[i][0][2] = dp[i-1][0][1] 
    dp[i][1][2] = dp[i-1][1][1] 
print((sum(dp[n][0])+sum(dp[n][1]))%M)