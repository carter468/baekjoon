# 크리보드
# Gold 5, DP

N = int(input())

dp = list(range(N+1))
for i in range(1,N+1):
    if i+1 <= N:
        dp[i+1] = max(dp[i+1],dp[i]+1)
    j = i+2
    while j < N:
        j += 1
        dp[j] = max(dp[j],dp[i]*(j-i-1))

print(dp[N])