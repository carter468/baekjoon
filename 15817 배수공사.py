# 배수 공사
# Gold 4, DP, knapsack

N,X = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

dp = [[0]*(X+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    l,c = arr[i]
    for j in range(X+1):
        for k in range(c+1):
            if j >= k*l:
                dp[i+1][j] += dp[i][j-k*l]
print(dp[N][X])