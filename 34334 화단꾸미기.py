# 화단 꾸미기
# Gold 1, DP, bitmask

N,M,K = map(int,input().split())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

dp = [[-10**9]*(1<<M) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
    for j in range(M):
        for k in range(1<<M):
            dp[i][k] = max(dp[i][k],dp[i-1][k]+A[i-1])
            if k>>j&1 == 0:
                nk = k|1<<j
                t = 0
                for l in range(K):
                    if i+l > N: break
                    t += A[i+l-1]*B[j]
                    dp[i+l][nk] = max(dp[i+l][nk],dp[i-1][k]+t)
print(max(dp[N]))