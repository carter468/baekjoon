# 햄최몇?
# Gold 1, DP

input()
arr = tuple(map(int,input().split()))

k = sum(arr)

dp = [[False]*(k+1) for _ in range(k+1)]
dp[0][0] = True
for a in arr:
    for i in range(k,-1,-1):
        for j in range(k,-1,-1):
            if i >= a: dp[i][j] |= dp[i-a][j]
            if j >= a: dp[i][j] |= dp[i][j-a]

result = 0
for i in range(k):
    for j in range(i+1):
        if dp[i][j] and j >= k-i-j:
            result = max(result,k-i-j)
print(result)