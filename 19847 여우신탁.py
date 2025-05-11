# 여우 신탁
# Gold 2, DP, probability

input()
arr = tuple(map(int,input().split()))

m = arr[0]
dp = [1]*m
for x in arr[1:]:
    if x < m:
        for i in range(x,m):
            dp[i%x] += dp[i]
        m = x

result = 0
for i in range(m):
    result += i*dp[i]
print(result/arr[0])