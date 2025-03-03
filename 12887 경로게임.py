# 경로 게임
# Gold 5, DP

M = int(input())
arr = [input() for _ in range(2)]

count = 0
for i in range(2):
    for j in range(M):
        count += arr[i][j] == '.'

dp = [[999]*M for _ in range(2)]
if arr[0][0] == '.': dp[0][0] = 1
if arr[1][0] == '.': dp[1][0] = 1
for i in range(1,M):
    if arr[0][i] == '.': dp[0][i] = dp[0][i-1]+1
    if arr[1][i] == '.': dp[1][i] = dp[1][i-1]+1
    dp[0][i] = min(dp[0][i],dp[1][i]+1)
    dp[1][i] = min(dp[1][i],dp[0][i]+1)

print(count-min(dp[0][-1],dp[1][-1]))