# Grazing2
# Gold 4, DP

import sys
input = sys.stdin.readline

N,S = map(int,input().split())
P = sorted([int(input()) for _ in range(N)])

d = (S-1)//(N-1)
k = S-1-d*(N-1)

dp = [[10**9]*(k+1) for _ in range(N)]
dp[0][0] = abs(P[0]-1)
for i in range(1,N):
    for j in range(min(k,i)+1):
        dp[i][j] = min(dp[i-1][max(0,j-1)],dp[i-1][j])+abs(1+d*i+j-P[i])
print(dp[-1][k])