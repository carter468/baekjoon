# Apples and Bananas
# Gold 4, game theory, DP

import sys
sys.setrecursionlimit(9999)

def solve(a,b,t):
    if (a,b) == (0,0): return 0
    if dp[a][b][t] != -1: return dp[a][b][t]

    for na,nb in (a-1,b),(a,b-1),(a-1,b-3),(a-3,b-1):
        if na >= 0 and nb >= 0:
            x = solve(na,nb,1-t)
            if x == 0:
                dp[a][b][t] = 1
                return 1

    dp[a][b][t] = 0
    return 0

a,b = map(int,input().split())

dp = [[[-1]*2 for _ in range(b+1)] for _ in range(a+1)]

print(('Bob','Alice')[solve(a,b,0)])