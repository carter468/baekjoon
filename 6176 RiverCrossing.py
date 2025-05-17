# River Crossing
# Gold 4, DP, prefix sum

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr = [M*2]+[int(input()) for _ in range(N)]
for i in range(N):
    arr[i+1] += arr[i]

dp = [0]+[sys.maxsize]*N
for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = min(dp[i],dp[i-j]+arr[j])
print(dp[N]-M)