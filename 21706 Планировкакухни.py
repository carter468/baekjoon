# Планировка кухни
# Platinum 5, DP

fac = [1]
for i in range(1,101):
    fac.append(fac[-1]*i)

A,B,N = map(int,input().split())
W = [int(input()) for _ in range(N)]

dp = [[[0]*(A+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1
for i,w in enumerate(W,1):
    for j in range(i):
        for k in range(A+1):
            dp[i][j][k] += dp[i-1][j][k]
            if k+w <= A:
                dp[i][j+1][k+w] += dp[i-1][j][k]

t = sum(W)
result = 0
for j in range(N+1):
    for k in range(A+1):
        if t-k <= B:
            result += dp[N][j][k]*fac[j]*fac[N-j]
print(result)