# 생태학
# Gold 2, DP, probability, combinatorics

def nCr(n,r):
    x = 1
    for i in range(r):
        x = x*(n-i)//(i+1)
    return x

N,C,D,M = map(int,input().split())

X = nCr(N,C)
dp = [[0]*(N+1) for _ in range(D+1)] # i번째 날에 j마리 부착되어있을 확률
dp[0][0] = 1
for i in range(1,D+1):
    for j in range(N+1):
        if dp[i-1][j] == 0: continue
        for k in range(C+1): # 새롭게 k마리 부착, 나머지 C-k는 이미 부착된 새
            if C-k > j or k > N-j: continue
            dp[i][j+k] += dp[i-1][j]*nCr(j,C-k)*nCr(N-j,k)/X

print(dp[D][M])