# 이친수

n = int(input())
dp = [[0,0] for _ in range(n)]
dp[0] = [0,1]

for i in range(1,n):
    dp[i][0] = dp[i-1][0]+dp[i-1][1]
    dp[i][1] = dp[i-1][0]
print(dp[-1][0]+dp[-1][1])