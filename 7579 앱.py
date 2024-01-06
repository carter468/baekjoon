# 앱
# Gold 3, DP, knapsack

n,m = map(int, input().split())
memory = tuple(map(int, input().split()))
cost = tuple(map(int, input().split()))

k = sum(cost)+1
dp = [0]*k
result = 10000
for i in range(n):
    w,v = cost[i],memory[i]
    for j in range(k-1,w-1,-1):
        dp[j] = max(dp[j-w]+v,dp[j])
        if dp[j] >= m:
            result = min(result,j)

print(result)