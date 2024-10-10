# 시간낭비
# Gold 2, DP

n = int(input())
arr = tuple(map(int,input().split()))

dp = [-1]*n
dp[0] = 0
i = 0
while i < n and arr[i] != 0:
    j = i+arr[i]
    if j < n:
        dp[j] = dp[i]+1
    i = j

for i in range(n-2,-1,-1):
    j = i-arr[i]
    if j < 0 or dp[i] == -1 or arr[i] == 0: continue
    dp[j] = max(dp[j],dp[i]+1)

for i in range(n):
    j = i+arr[i]
    if j >= n or dp[i] == -1 or arr[i] == 0: continue
    dp[j] = max(dp[j],dp[i]+1)

print(dp[-1])
