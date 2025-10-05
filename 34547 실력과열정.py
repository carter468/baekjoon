# 실력과 열정
# Gold 5, DP

N = int(input())
a,b,K = map(int,input().split())

X = a+b
dp = [[-10**9]*(X+1) for _ in range(N+1)]
dp[0][a] = 0
for i in range(1,N+1):
    for j in range(X+1):
        for k in range(X+1):
            if abs(j-k) < K: continue
            dp[i][j] = max(dp[i][j],dp[i-1][k]+j*(X-j))
print(max(dp[N]))