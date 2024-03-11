# 자동차경주대회
# Gold 4, DP

m,n = int(input()),int(input())
d = tuple(map(int,input().split()))
t = list(map(int,input().split()))+[0]

dp = [1<<40]*(n+2)
dp[0] = 0
for i in range(n+1):
    j = m
    k = i
    while k <= n and j-d[k] >= 0:
        dp[k+1] = min(dp[k+1],dp[i]+t[k])
        j -= d[k]
        k += 1

result = []
p = dp[-1]
i = n
while i > 0:
    if dp[i] == p:
        result.append(i)
        p -= t[i-1]
    i -= 1

print(dp[-1])
print(len(result))
print(*result[::-1])