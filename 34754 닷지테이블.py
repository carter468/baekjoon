# 닷지 테이블
# Gold 3, DP, difference array

import sys
input = sys.stdin.readline

K = int(input())

attack = [[[0]*(K+9) for _ in range(4)] for _ in range(4)]
for t in range(K):
    d,*arr = input().split()
    s,r,p = map(int,arr)
    s -= 1

    if d == 'U':
        for i in range(r):
            attack[i][s][t] += 1
            attack[i][s][min(K+1,t+p)] -= 1
    elif d == 'D':
        for i in range(4-r,4):
            attack[i][s][t] += 1
            attack[i][s][min(K+1,t+p)] -= 1
    elif d == 'L':
        for i in range(r):
            attack[s][i][t] += 1
            attack[s][i][min(K+1,t+p)] -= 1
    elif d == 'R':
        for i in range(4-r,4):
            attack[s][i][t] += 1
            attack[s][i][min(K+1,t+p)] -= 1

for i in range(4):
    for j in range(4):
        for k in range(K+1):
            attack[i][j][k] += attack[i][j][k-1]

dp = [[[K]*(K+1) for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        dp[i][j][0] = 0

for k in range(1,K+1):
    for i in range(4):
        for j in range(4):
            c = 1 if attack[i][j][k-1] > 0 else 0
            for x,y in (i,j),(i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if 0 <= x < 4 and 0 <= y < 4:
                    dp[i][j][k] = min(dp[i][j][k],dp[x][y][k-1]+c)

result = K
for i in range(4):
    for j in range(4):
        result = min(result,dp[i][j][K])
print(result)