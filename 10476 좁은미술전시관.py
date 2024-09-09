# 좁은 미술전시관
# Gold 4, DP

n,k = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n+1)]

dp = [[[10**9]*3 for _ in range(k+1)] for _ in range(n)]
dp[0][0][0] = 0
if k > 0: dp[0][1][1],dp[0][1][2] = arr[0]

result = sum(arr[0])
for i in range(1,n):
    result += sum(arr[i])
    for j in range(k+1):
        dp[i][j][0] = min(dp[i-1][j])
        if j > 0:
            dp[i][j][1] = min(dp[i-1][j-1][0],dp[i-1][j-1][1])+arr[i][0]
            dp[i][j][2] = min(dp[i-1][j-1][0],dp[i-1][j-1][2])+arr[i][1]
print(result-min(dp[-1][k]))
