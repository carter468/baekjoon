# Acka
# Gold 3, DP

def solve(n,a,b,c):
    if a < 0 or b < 0 or c < 0: return 0
    if n==0:
        if a == 0 and b == 0 and c == 0: return 1
        else: return 0
    if dp[n][a][b][c] != -1: return dp[n][a][b][c]

    dp[n][a][b][c] = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i == 0 and j == 0 and k == 0: continue
                dp[n][a][b][c] += solve(n-1,a-i,b-j,c-k)
    dp[n][a][b][c] %= 10**9+7
    return dp[n][a][b][c]

s,a,b,c = map(int,input().split())

dp = [[[[-1]*(s+1) for _ in range(s+1)] for _ in range(s+1)] for _ in range(s+1)]

print(solve(s,a,b,c))