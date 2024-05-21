# 꿀벌 승연이
# Gold 5, DP

M = 10**9+7

n,m = map(int,input().split())
arr = set([tuple(map(int,input().split())) for _ in range(int(input()))])

dp = [[0]*(m+1) for _ in range(n+1)]
dp[1][1] = 1
for j in range(1,m+1):
    for i in range(1,n+1):
        if (i,j) in arr:
            dp[i][j] = 0
            continue
        if j%2 == 0:
            for x,y in (i,j+1),(i+1,j+1),(i+1,j):
                if 1 <= x <= n and 1 <= y <= m:
                    dp[x][y] = (dp[x][y]+dp[i][j])%M
        else:
            for x,y in (i-1,j+1),(i,j+1),(i+1,j):
                if 1 <= x <= n and 1 <= y <= m:
                    dp[x][y] = (dp[x][y]+dp[i][j])%M

print(dp[n][m])