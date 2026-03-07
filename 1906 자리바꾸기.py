# 자리 바꾸기
# Platinum 3, DP, bitmask

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
cost = [[0]*K for _ in range(K)]
count = [0]*K
for _ in range(N):
    x = int(input())-1
    for i in range(K):
        cost[x][i] += count[i]
    count[x] += 1

dp = [sys.maxsize]*(1<<K)
dp[0] = 0
for s in range(1<<K):
    for i in range(K):
        if s>>i&1 == 0:
            c = 0
            for j in range(K):
                if s>>j&1 == 0 and i != j:
                    c += cost[i][j]
            ns = s|1<<i
            dp[ns] = min(dp[ns],dp[s]+c)
print(dp[-1])