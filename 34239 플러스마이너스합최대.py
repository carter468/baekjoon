# 플러스 마이너스 합 최대
# Gold 4, DP, Kadane's Algorithm

N = int(input())
A = tuple(map(int,input().split()))

if N == 1: exit(print(A[0]))

dp = [-10**9]*(N+1)
dp[1] = A[0]
for i in range(1,N):
    if i%2 == 0:
        dp[i+1] = max(dp[i]+A[i],A[i])
    else:
        dp[i+1] = dp[i]-A[i]
r1 = max(dp)

dp = [-10**9]*N
dp[1] = A[1]
for i in range(1,N-1):
    if i%2 == 0:
        dp[i+1] = max(dp[i]+A[i+1],A[i+1])
    else:
        dp[i+1] = dp[i]-A[i+1]
r2 = max(dp)

print(max(r1,r2))