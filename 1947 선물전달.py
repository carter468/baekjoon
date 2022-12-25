# 선물 전달
# Gold 3, 다이나믹 프로그래밍

n = int(input())
dp = [0]*1000001
dp[2] = 1
for i in range(3,n+1):
    dp[i] = (dp[i-1]+dp[i-2])*(i-1)%1000000000
print(dp[n])