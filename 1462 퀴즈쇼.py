# 퀴즈쇼
# Platinum 4, DP, prefix sum

N,M = map(int,input().split())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

psum = [0]
for a in A:
    psum.append(psum[-1]+a)
    
dp = [[-10**9]*2 for _ in range(N+1)]
dp[0][1] = 0
for i in range(1,N+1):
    a = A[i-1]
    b = B[i-1]
    dp[i][0] = max(dp[i-1])+a
    if i-M >= 0:
        dp[i][1] = dp[i-M][1]+psum[i]-psum[i-M]+b
    dp[i][1] = max(dp[i][1],max(dp[i-1])-a)

print(max(dp[N]))