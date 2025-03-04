# Baekjoon Database Management System
# Gold 4, DP

for _ in range(int(input())):
    N,M,C = map(int,input().split())
    cost = tuple(map(int,input().split()))
    arr = tuple(map(int,input().split()))

    dp = [[10**9]*(M+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        d = arr[i]
        for j in range(M+1): 
            if d == j: 
                dp[i+1][j] = min(dp[i+1][j],dp[i][j])
            else:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j]+cost[d-1])
                dp[i+1][d] = min(dp[i+1][d],dp[i][j]+C)
    
    print(min(dp[N]))