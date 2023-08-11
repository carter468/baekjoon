# 방 번호
# Gold 3, DP

N = int(input())
P = tuple(map(int,input().split()))
M = int(input())

dp = [-10**9]*(M+1)
for i in range(N-1,-1,-1):
    for j in range(P[i],M+1):
        dp[j] = max(dp[j],i,dp[j-P[i]]*10+i)

print(dp[M])