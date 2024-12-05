# Tile Exchanging
# Gold 3, DP, knapsack

N,M = map(int,input().split())
A = [int(input()) for _ in range(N)]

dp = [[10**9]*(M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(int(M**0.5)+1):
        a = j*j
        b = (A[i]-j)**2
        for k in range(a,M+1):
            dp[i+1][k] = min(dp[i+1][k],dp[i][k-a]+b)
print(dp[N][M] if dp[N][M] != 10**9 else -1)