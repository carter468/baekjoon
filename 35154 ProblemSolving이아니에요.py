# ProblemSolving이 아니에요
# Gold 4, DP

MOD = 998244353

dp = [[0]*2505 for _ in range(5005)]
dp[0][0] = 1
for i in range(1,5001):
    for j in range(i//2+1):
        dp[i][j] = (dp[i][j]+dp[i-2][j-1]+dp[i-1][j+1])%MOD

input()
for n in map(int,input().split()):
    if n == 1: print(-1)
    else: print(sum(dp[n])%MOD)