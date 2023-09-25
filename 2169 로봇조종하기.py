# 로봇 조종하기
# Gold 2, DP

n,m = map(int,input().split())
dp = [list(map(int,input().split())) for _ in range(n)]

for j in range(1,m):
    dp[0][j] += dp[0][j-1]
for i in range(1,n):
    left = [dp[i][j]+dp[i-1][j] for j in range(m)]
    right = [dp[i][j]+dp[i-1][j] for j in range(m)]
    for j in range(1,m):
        left[j] = max(left[j],left[j-1]+dp[i][j])
    for j in range(m-2,-1,-1):
        right[j] = max(right[j],right[j+1]+dp[i][j])
    for j in range(m):
        dp[i][j] = max(left[j],right[j])
        
print(dp[-1][-1])