# K의 배수
# Gold 3, DP

MOD = 10**9+7

N,M,K = map(int,input().split())
arr = tuple(map(int,input().split()))

dp = [[0]*K for _ in range(M)]
if M == 1:
    for a in arr:
        if a != 0:
            dp[0][a%K] += 1
    print(dp[0][0])
else:
    for a in arr:
        dp[0][a%K] += 1
    for i in range(1,M-1):
        for a in arr:
            for k in range(K):
                m = (k+a*10**i)%K
                dp[i][m] = (dp[i][m]+dp[i-1][k])%MOD
    for a in arr:
        if a != 0:
            for k in range(K):
                m = (k+a*10**(M-1))%K
                dp[M-1][m] = (dp[M-1][m]+dp[M-2][k])%MOD
    print(dp[-1][0])