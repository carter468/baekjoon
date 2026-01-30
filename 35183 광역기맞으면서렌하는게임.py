# 광역기 맞으면 서렌하는 게임
# Gold 5, DP

import sys
input = sys.stdin.readline

N = int(input())
dp = [[False]*2 for _ in range(1001)]
l,r = map(int,input().split())
for i in range(1,1001):
    if l <= i <= r:
        dp[i][0] = True
    else:
        dp[i][1] = True

for _ in range(N-1):
    ndp = [[False]*2 for _ in range(1001)]
    l,r = map(int,input().split())
    for i in range(1,1001):
        for j in (i-1,i,i+1):
            if j < 1 or j > 1000: continue
            if l <= j <= r:
                ndp[j][0] |= dp[i][0]
                ndp[j][1] |= dp[i][1]
            else:
                ndp[j][1] |= dp[i][0]
    dp = ndp

for i in range(1,1001):
    if any(dp[i]):
        print('World Champion')
        break
else:
    print('Surrender')