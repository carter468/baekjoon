# 격자 연결하기
# Gold 4, DP

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

result = -1000
dp1 = [[0]*M for _ in range(N)]
dp2 = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        dp1[i][j] = max(dp1[i-1][j],dp1[i][j-1],0)+arr[i][j]
        dp2[i][-1-j] = max(dp2[i-1][-1-j],dp2[i][-j],0)+arr[i][-1-j]
        result = max(result,dp1[i][j],dp2[i][-1-j])
print(result)