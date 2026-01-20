# FLEX
# Gold 2, DP

N,M = map(int,input().split())
C = tuple(map(int,input().split()))

# i일에 총 j만큼 추가 지출하고 당일 k를 지출했을때 최소 박탈감
dp = [[[10**9]*11 for _ in range(M+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(1,N+1):
    for k in range(C[i-1],11):
        t = k-C[i-1]
        for j in range(M+1-t):
            for l in range(11):
                dp[i][j+t][k] = min(dp[i][j+t][k],dp[i-1][j][l]+max(0,l-k)**2)

result = 10**9
for j in range(M+1):
    for k in range(11):
        result = min(result,dp[N][j][k])
print(result)