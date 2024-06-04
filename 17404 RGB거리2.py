# RGB거리 2
# Gold 4, DP

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

dp = [[[10**9]*3 for _ in range(3)] for _ in range(n)]
for i in range(3):
    dp[0][i][i] = arr[0][i]
    
for i in range(1,n-1):
    for j in range(3):
        for k in range(3):
            dp[i][j][k] = min(dp[i-1][j][k-1],dp[i-1][j][k-2])+arr[i][k]

result = 10**9
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i == k or j == k: continue
            result = min(result,dp[n-2][i][j]+arr[-1][k])
print(result)
