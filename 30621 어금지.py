# 어? 금지
# Gold 3, DP, binary search

import bisect

n = int(input())
t = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))
c = tuple(map(int,input().split()))

dp = [[0,0] for _ in range(n+1)]
for i in range(n):
    a = t[i]-b[i]
    j = bisect.bisect_left(t,a)
    dp[i+1][1] = max(dp[j])+c[i]
    dp[i+1][0] = max(dp[i])
print(max(dp[-1]))