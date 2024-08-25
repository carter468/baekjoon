# 기업투자
# Gold 2, DP, knapsack

n,m = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]

# m번째 기업까지 투자하고 n원을 썼을때 최대이익
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(n+1):
        v = 0 if j == 0 else arr[j-1][i] # i번째 회사에 j원 투자했을때 이익
        for k in range(j,n+1):
            dp[i][k] = max(dp[i][k],dp[i-1][k-j]+v)

x = dp[m][n]
print(x)
y = n
result = [0]*m
for i in range(m,0,-1):
    for j in range(1,n+1): 
        v = arr[j-1][i]
        if x-v == dp[i-1][y-j]:
            result[i-1] = j
            x -= v
            y -= j
            break
print(*result)
