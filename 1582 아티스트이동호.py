# 아티스트 이동호
# Platinum 4, DP

N,M,K = map(int,input().split())
P = [input() for _ in range(N)]

dp = [[0]*3333 for _ in range(N+1)]
for i in range(1,N+1):
    c = [0]*(M+1)
    for j in range(M):
        c[j+1] = c[j]+(P[i-1][j] == 'B')

    dp1 = [[0]*(M+1) for _ in range(M+1)]
    for j in range(1,M+1):
        for k in range(j):
            a = c[j]-c[k]
            b = j-k-a
            t = max(a,b)
            for l in range(k+1):
                dp1[j][l+1] = max(dp1[j][l+1],dp1[k][l]+t)
                dp1[j][l] = max(dp1[j][l],dp1[k][l])

    for j in range(i*M):
        for k in range(M+1):
            dp[i][j+k] = max(dp[i][j+k],dp[i-1][j]+dp1[M][k])

print(N*M-max(dp[N][:K+1]))