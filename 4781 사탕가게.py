# 사탕 가게
# Gold 4, DP, knapsack

import sys
input = sys.stdin.readline

while True:
    n,m = input().split()
    if n == '0': break
    
    n,m = int(n),int(float(m)*100+0.5)
    arr = []
    for _ in range(n):
        c,p = input().split()
        arr.append((int(c),int(float(p)*100+0.5)))
    
    dp = [0]*(m+1)
    for c,p in arr:
        for i in range(p,m+1):
            dp[i] = max(dp[i],dp[i-p]+c)
    print(dp[m])