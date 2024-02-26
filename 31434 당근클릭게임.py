# 당근 클릭 게임
# Gold 3, DP

n,k = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]

dp = [[-1]*5002 for _ in range(k+1)]
dp[0][1] = 0
for i in range(1,k+1):
    for j in range(1,5002):
        for a,b in arr:
            if dp[i-1][j] >= a and j+b < 5002:
                dp[i][j+b] = max(dp[i][j+b],dp[i-1][j]-a)
        if dp[i-1][j] != -1:
            dp[i][j] = max(dp[i][j],dp[i-1][j]+j)
print(max(dp[k]))