# Dairy Queen
# Gold 5, DP, knapsack

N,C = map(int,input().split())

dp = [1]+[0]*N
for _ in range(C):
    ndp = [0]*(N+1)
    for i in range(0,N+1,int(input())):
        for j in range(i,N+1):
            ndp[j] += dp[j-i]
    dp = ndp
print(dp[N])