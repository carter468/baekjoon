# 입 챌린저
# Gold 3, DP, knapsack

n,m,p = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]

dp = [[10**9]*(m+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    a,b = arr[i]
    for j in range(101):
        c = a*j+p*j*(j-1)//2
        d = b*j
        if d > m: break
        for k in range(d,m+1):
            dp[i+1][k] = min(dp[i+1][k],dp[i][k-d]+c)
print(dp[n][m])
