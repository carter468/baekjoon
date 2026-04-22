# 테트리스
# Platinum 2, DP, case work

MOD = 10**6

N = int(input())

dp = [[0]*7 for _ in range(N+5)]
dp[0][0] = 1
for i in range(N):
    dp[i+2][0] = (dp[i+2][0]+dp[i][3]+dp[i][6]+dp[i][5])%MOD
    dp[i+3][0] = (dp[i+3][0]+dp[i][1]*2+dp[i][4]*2+dp[i][2]*2)%MOD

    dp[i+1][6] = (dp[i+1][6]+dp[i][1]+dp[i][4])%MOD
    dp[i+2][6] = (dp[i+2][6]+dp[i][0]*2)%MOD
    dp[i+4][6] = (dp[i+4][6]+dp[i][3]+dp[i][5])%MOD
    dp[i+5][6] = (dp[i+5][6]+dp[i][1]*2)%MOD

    dp[i+1][3] = (dp[i+1][3]+dp[i][1]+dp[i][4])%MOD
    dp[i+2][3] = (dp[i+2][3]+dp[i][0]*2)%MOD
    dp[i+4][3] = (dp[i+4][3]+dp[i][6]+dp[i][5])%MOD
    dp[i+5][3] = (dp[i+5][3]+dp[i][4]*2)%MOD

    dp[i+1][1] = (dp[i+1][1]+dp[i][0])%MOD
    dp[i+3][1] = (dp[i+3][1]+dp[i][3]*2+dp[i][5])%MOD
    dp[i+4][1] = (dp[i+4][1]+dp[i][4])%MOD

    dp[i+1][4] = (dp[i+1][4]+dp[i][0])%MOD
    dp[i+3][4] = (dp[i+3][4]+dp[i][6]*2+dp[i][5])%MOD
    dp[i+4][4] = (dp[i+4][4]+dp[i][1])%MOD

    dp[i+2][5] = (dp[i+2][5]+dp[i][0]*2)%MOD

    dp[i+1][2] = (dp[i+1][2]+dp[i][0])%MOD
    dp[i+3][2] = (dp[i+3][2]+dp[i][5]*2+dp[i][6]+dp[i][3])%MOD
    dp[i+4][2] = (dp[i+4][2]+dp[i][4]+dp[i][1])%MOD
print(dp[N][0])