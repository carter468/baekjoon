# 수확
# Gold 3, DP

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solve(l,r):
    if dp[l][r] != -1: return dp[l][r]
    if l != 0: dp[l][r] = solve(l-1,r)+(l+r)*V[l-1]
    if r != 0: dp[l][r] = max(dp[l][r],solve(l,r-1)+(l+r)*V[-r])
    return dp[l][r]

N = int(input())
V = [int(input()) for _ in range(N)]

dp = [[-1]*(N+1) for _ in range(N+1)]
dp[0][0] = 0
result = 0
for i in range(N):
    result = max(result,solve(i,N-i))
print(result)