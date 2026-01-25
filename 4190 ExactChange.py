# Exact Change
# Gold 5, DP

import sys
input = sys.stdin.readline
MAX = 20000

for _ in range(int(input())):
    X = int(input())

    dp = [0]+[MAX]*MAX
    for _ in range(int(input())):
        a = int(input())
        ndp = [MAX]*MAX
        for i in range(MAX):
            if i+a < MAX:
                ndp[i+a] = min(ndp[i+a],dp[i]+1)
            ndp[i] = min(ndp[i],dp[i])
        dp = ndp

    for i in range(X,MAX):
        if dp[i] < MAX:
            print(i,dp[i])    
            break