# 동전 2
# Gold 5, DP

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
value = [int(input()) for _ in range(n)]

dp = [0]+[10001]*k
for i in range(1,k+1): 
    for v in value:
        if v <= i:
            dp[i] = min(dp[i],dp[i-v]+1)

print(dp[k] if dp[k]<10001 else -1)