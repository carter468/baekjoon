# 점프
# Gold 4, DP

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
s = set([int(input()) for _ in range(M)])

K = int((N*2)**0.5)+1
dp = [[N]*K for _ in range(N+1)]
dp[1][0] = 0
for i in range(1,N):
    for j in range(K):
        for k in (j-1,j,j+1):
            if 0 < k < K and i+k <= N and i+k not in s:
                dp[i+k][k] = min(dp[i+k][k],dp[i][j]+1)

result = min(dp[N])
print(result if result != N else -1)