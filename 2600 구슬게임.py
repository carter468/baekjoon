# 구슬게임
# Gold 4, DP, game theory

import sys
sys.setrecursionlimit(10**4)

def solve(x,y):
    if dp[x][y] != -1: return dp[x][y]

    dp[x][y] = 0
    for b in B:
        if x-b >= 0 and solve(x-b,y) == 0:
            dp[x][y] = 1
            return 1
        if y-b >= 0 and solve(x,y-b) == 0:
            dp[x][y] = 1
            return 1
    return 0

B = tuple(map(int,input().split()))

dp = [[-1]*501 for _ in range(501)]
for _ in range(5):
    print('BA'[solve(*map(int,input().split()))])