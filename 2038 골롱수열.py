# 골롱 수열
# Gold 2, 다이나믹 프로그래밍

n = int(input())

dp = [0]*1000001
dp[1] = 1
total = 1
i = 1
while total<n:
    i += 1
    dp[i] = 1+dp[i-dp[dp[i-1]]]
    total += dp[i]
print(i)