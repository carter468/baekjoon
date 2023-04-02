# 타일 밟기
# Gold 1, DP

n = int(input())
arr = tuple(map(int,input().split()))

max_val = max(arr)
check = [-1]*(max_val+1)
for i,a in enumerate(arr):
    check[a] = i

dp = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        d = arr[j]-arr[i]
        if arr[j]+d <= max_val and check[arr[j]+d] != -1:
            dp[i][j] = arr[i]+arr[j]

for i in range(n-1):
    for j in range(n):
        if dp[i][j]:
            d = abs(arr[i]-arr[j])
            if (k:=arr[j]+d) <= max_val and check[k] != -1:
                dp[j][check[k]] = max(dp[j][check[k]],dp[i][j]+arr[check[k]])

result = 0
for i in dp:
    result = max(result,max(i))

print(result)