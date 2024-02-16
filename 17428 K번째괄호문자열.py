# K번째 괄호 문자열
# Platinum 5, DP

def solve(i,j,k):
    if i == 1: return ')'
    if k < dp[i-1][j+1]: return '('+solve(i-1,j+1,k)
    else: return ')'+solve(i-1,j-1,k-dp[i-1][j+1])

n,k = map(int,input().split())

dp = [[0]*(n+2) for _ in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
    for j in range(i+1):
        if j == 0: dp[i][j] = dp[i-1][j+1]
        else: dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

if k >= dp[n][0]: print(-1)
else: print(solve(n,0,k))