# 팰린드롬 개수 구하기 (Large)
# Platinum 5, DP

MOD = 10007

S = input()

N = len(S)
dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for l in range(2,N+1):
    for i in range(N-l+1):
        j = i+l-1
        if S[i] != S[j]:
            dp[i][j] = (dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1])%MOD
        else:
            dp[i][j] = (dp[i+1][j]+dp[i][j-1]+1)%MOD
print(dp[0][N-1])