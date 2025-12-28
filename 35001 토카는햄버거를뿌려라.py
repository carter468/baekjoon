# 토카는 햄버거를 뿌려라
# Platinum 5, DP, bitmask

MOD = 10**9+7

N,M = map(int,input().split())
A = tuple(map(int,input().split()))

dp = [[0]*(1<<N) for _ in range(M+1)]
dp[0][0] = 1
for i in range(1<<N):
    t = 0
    c = 0
    for j in range(N):
        if i>>j&1: c += 1
        else: t += A[j]**2
    if t == 0 or c >= M: continue
    t = pow(t,-1,MOD)
    for j in range(N):
        if i>>j&1 == 0:
            ni = i|1<<j
            dp[c+1][ni] = (dp[c+1][ni]+dp[c][i]*A[j]**2*t)%MOD

result = 0
for i in range(1<<N):
    if i&1:
        result = (result+dp[M][i])%MOD
print(result)