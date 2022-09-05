# 할 일 정하기 1

n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int,input().split())))

dp = [10**6]*(1<<n)
dp[0] = 0

for i in range(1<<n):
    k = 0
    for j in range(n):
        if i&(1<<j):
            k += 1
    for j in range(n):
        if i&(1<<j) == 0 and dp[i|(1<<j)] > dp[i] + cost[k][j]:
            dp[i|(1<<j)] = dp[i] + cost[k][j]
print(dp[-1])