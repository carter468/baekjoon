# 그룹 나누기 (Subset)
# Gold 4, DP

N = int(input())

if (N*(N+1)//2)%2 == 1: exit(print(0))
M = N*(N+1)//4
dp = [1]+[0]*M

for i in range(1,N+1):
    for j in range(M,-1,-1):
        if i+j <= M:
            dp[i+j] += dp[j]
print(dp[M]//2)