# m-ary Partitions
# Gold 5, DP

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K,M,N = map(int,input().split())

    dp = [[0]*10 for _ in range(N+1)]
    for j in range(10):
        dp[0][j] = 1

    for i in range(1,N+1):
        for j in range(10):
            k = M**j
            if i >= k:
                dp[i][j] = dp[i-k][j]+dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    
    print(K,dp[N][-1])