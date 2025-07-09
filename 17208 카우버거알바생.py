# 카우버거 알바생
# Gold 4, DP, knapsack

N,M,K = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

dp = [[-999]*(K+1) for _ in range(M+1)]
dp[0][0] = 0
result = 0
for x,y in arr:
    ndp = [[-999]*(K+1) for _ in range(M+1)]
    for i in range(M+1):
        for j in range(K+1):
            if i < x or j < y:
                ndp[i][j] = dp[i][j]
            else:
                ndp[i][j] = max(dp[i][j],dp[i-x][j-y]+1)
            result = max(result,ndp[i][j])
    dp = ndp
print(result)