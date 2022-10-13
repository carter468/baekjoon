# 병사 배치하기

n = int(input())
arr = list(map(int,input().split()))

dp = [0]*n
arr_len = 0
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if arr[j] > arr[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j] + 1
print(n - max(dp))