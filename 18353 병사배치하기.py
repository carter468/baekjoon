# 병사 배치하기

n = int(input())
arr = list(map(int,input().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if arr[j] > arr[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
print(n - max(dp))