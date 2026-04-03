# Candy
# Gold 2, DP

N,F,T = map(int,input().split())
A = tuple(map(int,input().split()))

m = N*(N-1)//2
dp = [[-10**22]*(m+1) for _ in range(F+1)]
dp[0][0] = 0
for k,a in enumerate(A):
    for i in range(F-1,-1,-1):
        for j in range(m-k,-1,-1):
            dp[i+1][j+k] = max(dp[i+1][j+k],dp[i][j]+a)

for j in range(m+1):
    if dp[F][j] >= T:
        print(j-F*(F-1)//2)
        break
else: print('NO')