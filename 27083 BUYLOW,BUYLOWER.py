# BUY LOW, BUY LOWER
# Gold 4, DP

N = int(input())
A = []
for _ in range((N-1)//10+1):
    A += map(int,input().split())

dp = [1]*N 
for i in range(N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i],dp[j]+1)
max_len = max(dp)

count = [0]*N
for i in range(N):
    if dp[i] == 1: count[i] = 1
    else:
        last = 0
        for j in range(i-1,-1,-1):
            if A[j] > A[i] and dp[j] == dp[i]-1 and A[j] != last:
                count[i] += count[j]
                last = A[j]

total_count = 0
last = 0
for i in range(N-1,-1,-1):
    if dp[i] == max_len and A[i] != last:
        total_count += count[i]
        last = A[i]

print(max_len,total_count)