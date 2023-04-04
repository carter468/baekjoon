# 영훈이의 색칠공부
# Gold 1, DP

MOD = 1000000007

n = int(input())

dp = [0]*(n+1)
if n > 1:
    dp[2] = 1
for i in range(3,n+1):
    dp[i] = (dp[i-1]+dp[i-2])*(i-1)%MOD
result = dp[n]
for i in range(2,n+1):
    result = result*i%MOD

print(result)