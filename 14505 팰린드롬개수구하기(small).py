# 팰린드롬 개수 구하기(small)
# Gold 3, DP

l = len((s := input()))

dp = [[0]*l for _ in range(l)]
for i in range(l):
    dp[i][i] = 1
    if i+1 < l:
        dp[i][i+1] = 2 + (s[i] == s[i+1])

for i in range(2,l):
    for j in range(l):
        if (k := i+j) >= l: break
        dp[j][k] = dp[j+1][k]+dp[j][k-1] + (1 if s[j] == s[k] else -dp[j+1][k-1])

print(dp[0][l-1])