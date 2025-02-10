# 알고리즘 기말고사
# Gold 2, DP

def solve(n,k):
    if dp[n][k] != 0: return dp[n][k]
    
    dp[n][k] = solve(n,k-1)-solve(n-1,k-1)
    return dp[n][k]

M = 17
dp = [[0]*(M+1) for _ in range(M+1)]
f = 1
for i in range(M+1):
    dp[i][0] = f
    f *= i+1
solve(M,M)

for _ in range(int(input())):
    t,N,K = map(int,input().split())
    print(t,dp[N][K])