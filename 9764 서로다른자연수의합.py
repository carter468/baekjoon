# 서로 다른 자연수의 합
# Gold 5, DP

M = 100999
N = 2001

dp = [[0]*N for _ in range(N)]
for i in range(1,N):
    for j in range(1,N):
        if j < i:
            dp[i][j] = (dp[i][j-1]+dp[i-j][j-1])%M
        elif j > i:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = (dp[i][j-1]+1)%M

for _ in range(int(input())):
    n = int(input())
    print(dp[n][n])