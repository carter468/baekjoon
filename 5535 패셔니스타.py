# 패셔니스타
# Gold 4, DP

d,n = map(int,input().split())
t = [int(input()) for _ in range(d)]
arr = [tuple(map(int,input().split())) for _ in range(n)]

dp = [[-10**9]*n for _ in range(d)]
for i in range(n):
    if arr[i][0] <= t[0] <= arr[i][1]: dp[0][i] = 0
for i in range(d):
    for j in range(n):
        if arr[j][0] <= t[i] <= arr[j][1]:
            for k in range(n):
                dp[i][j] = max(dp[i][j],dp[i-1][k]+abs(arr[j][2]-arr[k][2]))
print(max(dp[-1]))
