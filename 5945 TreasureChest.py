# Treasure Chest
# Gold 3, DP, game theory, prefix sum

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

psum = [0]
for i in range(N):
    psum.append(psum[-1]+arr[i])

dp = [0]*N
for i in range(N):
    dp[i] = arr[i]
for l in range(2,N+1):
    ndp = [0]*N
    for i in range(N-l+1):
        ndp[i] = psum[i+l]-psum[i]-min(dp[i+1],dp[i])
    dp = ndp

print(dp[0])