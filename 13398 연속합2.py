# 연속합 2
# Gold 5, DP

dp = [[-1000]*2 for _ in range(int(input())+2)]
result = -1000
for i,a in enumerate(map(int,input().split())):
    dp[i][0] = max(dp[i-1][0]+a,a)
    dp[i][1] = max(dp[i-2][0]+a,dp[i-1][1]+a,a)
    result = max(result,max(dp[i]))
print(result)