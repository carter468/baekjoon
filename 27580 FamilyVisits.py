# Family Visits
# Gold 3, DP

import sys
input = sys.stdin.readline
INF = 10**9

N,D = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

result = 0
p = 1
for _ in range(D):
    V = int(input())
    dp = [[INF]*(N+1) for _ in range(N+1)]
    dp[p-1] = [0]*(N+1)

    for i in range(p,V+1):
        dp[i][0] = dp[i-1][0]+arr[i-1][0]
        for j in range(1,i-p+2):
            dp[i][j] = max(0,min(dp[i-1][j-1]+arr[i-1][0]-arr[i-1][1],dp[i-1][j]+arr[i-1][0]))
    
    for i in range(V-p+2):
        if dp[V][i] == 0:
            result += i
            break
    else: exit(print(-1))

    p = V+1

print(result)