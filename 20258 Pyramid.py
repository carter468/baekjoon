# Pyramid
# Platinum 4, DP

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N,K = map(int,input().split())

    dp = [K-1]
    pos = 0
    for i in range(N-1):
        pos += dp[pos]%2
        ndp = [0]*(i+2)
        for j in range(i+1):
            ndp[j] += (dp[j]+1)//2
            ndp[j+1] += dp[j]//2
        dp = ndp
    print(pos)