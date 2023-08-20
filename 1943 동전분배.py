# 동전 분배
# Gold 3, DP, knapsack

import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    coin,s = [],0
    for i in range(n):
        a,b = map(int,input().split())
        coin.append((a,b))
        s += a*b
    if s%2 == 1: print(0)
    else:
        s //= 2
        dp = [1]+[0]*s
        for i in range(n):
            a,b = coin[i]
            for j in range(s,a-1,-1):
                if dp[j-a]:
                    for k in range(b):
                        if j+k*a > s: break
                        dp[j+k*a] = 1
        print(dp[s])