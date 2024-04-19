# 파이프 옮기기 1
# Gold 5, DP

n = int(input())
arr = [input().split() for _ in range(n)]

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1': continue
        dp[i][j][0] += dp[i][j-1][0]+dp[i][j-1][2]
        dp[i][j][1] += dp[i-1][j][1]+dp[i-1][j][2]
        if i > 0 and j > 0 and arr[i-1][j] == '0' and arr[i][j-1] == '0':
            dp[i][j][2] += sum(dp[i-1][j-1])
print(sum(dp[-1][-1]))