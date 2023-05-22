# 합분해
# Gold 5, DP

n,k = map(int,input().split())

dp = [[0]*(n+1) for _ in range(k)]
dp[0] = [1]*(n+1)
for i in range(1,k):
    for j in range(n+1):
        for k in range(n+1-j): 
            dp[i][j+k] += dp[i-1][j]
print(dp[-1][-1]%10**9)