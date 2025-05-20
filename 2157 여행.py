# 여행
# Gold 4, DP

import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    a,b,c = map(int,input().split())
    arr[a][b] = max(arr[a][b],c)

dp = [[-1]*(M+1) for _ in range(N+1)]
dp[1][1] = 0
for i in range(2,N+1):
    for j in range(1,i):
        c = arr[j][i]
        if c == 0: continue
        for k in range(1,min(i,M)):
            if dp[j][k] != -1:
                dp[i][k+1] = max(dp[i][k+1],dp[j][k]+c)

print(max(0,max(dp[N])))