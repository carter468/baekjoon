# 다항식 게임
# Gold 4, DP

dp = [[0]*400 for _ in range(400)]
dp[1][0],dp[1][1] = 1,1
for i in range(2,21):
    for j in range(300):
        for k in range(i+1):
            dp[i][j+k] += dp[i-1][j]

for _ in range(int(input())):
    k,n = map(int,input().split())
    print(dp[k][n])