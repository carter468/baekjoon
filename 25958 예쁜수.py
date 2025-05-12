# 예쁜수
# Gold 4, DP, knapsack

M,K = map(int,input().split())

arr = []
for i in range(1,M+1):
    if i%sum(int(j) for j in str(i)) == 0: arr.append(i)

dp = [0]*(M+1)
for a in arr:
    dp[a] += 1
    for i in range(a,M+1):
        dp[i] = (dp[i]+dp[i-a])%K

print(dp[M]%K)