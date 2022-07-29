# 가장 긴 증가하는 부분수열4

n = int(input())
arr = list(map(int,input().split()))

dp = [1]*n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)

cnt = max(dp)
print(cnt)

ans = []
idx = n-1
while idx >= 0:
    if dp[idx] == cnt:
        ans.append(arr[idx])
        cnt -= 1
    idx -= 1

print(*reversed(ans))