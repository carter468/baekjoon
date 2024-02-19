# 입대
# Gold 3, DP

n,m = map(int,input().split())
arr = tuple(map(int,input().split()))
a,d = map(int,input().split())

dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(n): 
        dp[i][j] = max(dp[i-1][j]+arr[i-1],dp[i][j])
    if i >= d:
        for j in range(n): 
            dp[i][j+1] = max(dp[i-d][j]+a,dp[i][j+1])
    if i == n:
        for j in range(n):
            dp[i][j+1] = max(dp[i-1][j]+a,dp[i][j+1])

result = -1
for i in range(n+1):
    if dp[-1][i] >= m:
        result = i
        break
print(result)