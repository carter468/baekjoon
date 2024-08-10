# 도트 매트릭스 프린터
# Gold 4, DP

s = input()
dp = [[[10**9]*27 for _ in range(26)] for _ in range(len(s))]

dp[0][ord(s[0])-65][-1] = 2
for i in range(1,len(s)):
    c = ord(s[i])-65
    for j in range(26):
        for k in range(27):
            if j == c: dp[i][c][k] = min(dp[i][c][k],dp[i-1][j][k]+1)
            else: dp[i][c][k] = min(dp[i][c][k],dp[i-1][j][k]+2)
            dp[i][j][c] = min(dp[i][j][c],dp[i-1][j][k]+2)

result = 10**9
for j in range(26):
    for k in range(27):
        result = min(result,dp[-1][j][k])
print(result)
