# 사건은 다가와 (Easy)
# Gold 5, DP

n = int(input())
arr = [0]*1001
for _ in range(n):
    t,a,b = map(int,input().split())
    arr[t] = (a,b)

dp = [9999]*2003
dp[1000] = 0
for i in range(1,1001):
    dp1 = [9999]*2003
    for j in range(2001):
        if arr[i] != 0:
            a,b = arr[i]
            if a < j-1000 < b:
                dp1[j] = 9999
                continue
        dp1[j] = min(dp[j-1]+1,dp[j],dp[j+1]+1)
    dp = dp1
result = min(dp)
print(-1 if result == 9999 else result)
