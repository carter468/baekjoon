# 변형 계단 수
# Gold 3, DP

M = 10**9+7

n = int(input())

if n == 1: print(10) 
else:
    dp = [[[0]*4 for _ in range(10)] for _ in range(n)] 
    for i in range(10):
        if i > 0: dp[1][i][0] = 1
        if i < 9: dp[1][i][2] = 1
    for i in range(1,n-1):
        for j in range(10):
            if j > 0:
                dp[i+1][j-1][2] += (dp[i][j][0]+dp[i][j][1])%M
                dp[i+1][j-1][3] += dp[i][j][2]%M
            if j < 9:
                dp[i+1][j+1][0] += (dp[i][j][2]+dp[i][j][3])%M
                dp[i+1][j+1][1] += dp[i][j][0]%M
    
    result = 0
    for i in range(10):
        for j in range(4):
            result = (result+dp[-1][i][j])%M
    print(result)