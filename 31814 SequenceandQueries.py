# Sequence and Queries
# Gold 3, DP

n = int(input())
arr = tuple(map(int,input().split()))

result = 0
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if arr[i] <= arr[j]: dp[i][j] = dp[i+1][j+1]+1
        else: dp[i][j] = 0
        result += dp[i][j]

print(result)