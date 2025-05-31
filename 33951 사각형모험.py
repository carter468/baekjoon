# 사각형 모험
# Gold 2, DP, math

import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
arr = [input() for _ in range(N)]

dp1 = [[9999]*M for _ in range(N)]
dp2 = [[0]*M for _ in range(N)]
dp1[0][0] = 0
if arr[0][0] == 'A':
    dp1[0][0],dp2[0][0] = 1,1
for i in range(N):
    for j in range(M):
        if (i,j) == (0,0): continue
        dp1[i][j] = min(dp1[i-1][j],dp1[i][j-1])
        dp2[i][j] = max(dp2[i-1][j],dp2[i][j-1])
        if arr[i][j] == 'A':
            dp1[i][j] += 1
            dp2[i][j] += 1

T = N+M-1
for _ in range(K):
    a,b,c = map(int,input().split())
    result = 'NO'
    if a == b:
        if a*T == c: result = 'YES'
    elif (c-b*T)%(a-b) == 0:
        x = (c-b*T)//(a-b)
        if dp1[-1][-1] <= x <= dp2[-1][-1]: result = 'YES'
    print(result)