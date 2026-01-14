# 트윈 타워 (Easy)
# Gold 3, DP

N = int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

dp = [[[-10**22]*3 for _ in range(N+1)] for _ in range(N+1)]
dp[1][1][1] = A[0]
dp[1][0][0] = 0
for i in range(2,N+1):
    a = A[i-1]
    b = B[i-2]
    for j in range(i):
        dp[i][j][0] = max(dp[i-1][j])
        dp[i][j+1][1] = max(dp[i-1][j])+a
        dp[i][j+1][2] = dp[i-1][j][1]+a+b

result = [0]*(N+1)
for j in range(1,N+1):
    result[j] = max(result[j],max(dp[N][j]))
print(*result[1:],sep='\n')