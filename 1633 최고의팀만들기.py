# 최고의 팀 만들기
# Gold 4, DP

dp = [[[0]*16 for _ in range(16)] for _ in range(1000)]

for k in range(1,1001):
    try:
        a,b = map(int,input().split())
        for i in range(16):
            for j in range(16):
                dp[k][i][j] = dp[k-1][i][j]
                if i > 0: dp[k][i][j] = max(dp[k][i][j],dp[k-1][i-1][j]+a)
                if j > 0: dp[k][i][j] = max(dp[k][i][j],dp[k-1][i][j-1]+b)
    except:
        break
print(dp[k-1][15][15])