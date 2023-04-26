# 주사위 게임
# Gold 4, DP, 수학

n = int(input())

dp = [0]*1000001
dp[1] = 1
for i in range(2,n+1):
    for j in range(1,7):
        dp[i] += (dp[i-j]+1)/6

print(dp[n])