# 들판 건너가기
# Gold 4, DP

input()

dp = [-10**20]*101
for a in map(int,input().split()):
    dp[a] = max(0,dp[a])
    for i in range(1,101):
        dp[a] = max(dp[a],dp[i]+(a-i)**2)

print(max(dp))