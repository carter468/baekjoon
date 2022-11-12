# 리그 오브 레전설(small)
# Silver 1, 다이나믹프로그래밍

n,m = map(int,input().split())
dp = [0]*(n+1)
dp[1] = 1
if m<=n:
    dp[m] = 1
for i in range(1,n+1):
    if dp[i]:
        if i+1<=n:
            dp[i+1] += dp[i]
        if i+m<=n:
            dp[i+m] += dp[i]
print(dp[-1]%1000000007)