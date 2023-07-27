# 책 정리
# Gold 2, 가장 긴 증가하는 부분 수열 O(nlogn)

import bisect

n = int(input())
arr = tuple(map(int, input().split()))

dp = [arr[0]]
for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(n-len(dp))