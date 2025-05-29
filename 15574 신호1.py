# 신호 1
# Gold 4, DP

import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([tuple(map(int,input().split())) for _ in range(N)])

dp = [0]*N
for i in range(1,N):
    x1,y1 = arr[i]
    for j in range(i):
        x2,y2 = arr[j]
        if x1 == x2: break
        dp[i] = max(dp[i],dp[j]+((x1-x2)**2+(y1-y2)**2)**0.5)
print(max(dp))