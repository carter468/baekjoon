# 징검다리 건너기
# Gold 1, DP

# bottom-up, 572ms

N,K = map(int,input().split())
dp = [[0]*(N+1) for _ in range(K+2)]
dp[1][0] = 1
for i in range(1,K+1):
    for j in range(N):
        dp[i][j+1] = (dp[i][j]+dp[i-1][j]+dp[i-2][j])/3

result = 0
for i in range(1,K+1):
    result += dp[i][N]
print(result)

# top-down, 4500ms

# import sys
# sys.setrecursionlimit(10**7)

# def solve(k,n,r):
#     if k == 0: return 0
#     if n == 0: return 1
#     if dp[k][n][r] >= 0: return dp[k][n][r]

#     if r == 0: dp[k][n][r] = solve(k-1,n-1,1)/2+solve(k,n-1,1)/2
#     elif r == 1: dp[k][n][r] = solve(k-1,n,0)*2/3+solve(k,n-1,1)/3
#     return dp[k][n][r]

# N,K = map(int,input().split())
# dp = [[[-1]*2 for _ in range(N+1)] for _ in range(K+1)]

# print(solve(K,N,1))