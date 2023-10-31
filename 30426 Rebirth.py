# Rebirth
# Gold 4, DP

import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
move = [tuple(map(int,input().split())) for _ in range(k)]
ban = [0]*n
for _ in range(int(input())):
    ban[int(input())] = 1

dp = [[0]*n for _ in range(k+1)]
dp[0][m] = 1
for i in range(k):
    a,b = move[i]
    for j in range(n):
        c,d = (j+a)%n,(j+b)%n
        if dp[i][j] == 1:
            if ban[c] == 0:
                dp[i+1][c] = 1
            if ban[d] == 0:
                dp[i+1][d] = 1
print(('dystopia','utopia')[dp[k][0]])