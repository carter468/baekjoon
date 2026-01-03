# 균형의 창조자
# Gold 3, DP

N,I,G = map(int,input().split())

dp = [[[-10**9]*(I+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(1,N+1):
    a,b = map(int,input().split())
    for j in range(i):
        for k in range(I+1):
            x = min(I,k+a)
            dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k])
            dp[i][j+1][x] = max(dp[i][j+1][x],dp[i-1][j][k]+b)

for j in range(1,N+1):
    if dp[N][j][I] >= G:
        print(j)
        break
else: print(-1)