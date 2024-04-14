# DDR 체력 관리
# Gold 5, DP

n,k = map(int,input().split())
s = tuple(map(int,input().split()))
h = tuple(map(int,input().split()))

dp = [[-1]*101 for _ in range(n+1)]
dp[0][100] = 0
for i in range(1,n+1):
    a = h[i-1]
    b = s[i-1]
    for j in range(101):
        if dp[i-1][j] == -1: continue
        x = min(100,j+k)
        if x-a >= 0:
            dp[i][x-a] = max(dp[i][x-a],dp[i-1][j]+b)
        dp[i][x] = max(dp[i][x],dp[i-1][j])
print(max(dp[-1]))