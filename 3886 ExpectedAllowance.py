# Expected Allowance
# Gold 5, bruteforcing

def solve(c,x):
    if c == n:
        count[x] += 1
        return
    for i in range(1,m+1):
        solve(c+1,x+i)

while True:
    n,m,k = map(int,input().split())
    if n == 0: break

    count = [0]*(n*m+1)
    solve(0,0)

    result = 0
    for i in range(n*m+1):
        result += count[i]*max(1,i-k)
    print(result/m**n)

# DP

while True:
    N,M,K = map(int,input().split())
    if N == 0: break

    dp = [[0]*(N*M+1) for _ in range(N+1)]
    for j in range(1,M+1):
        dp[1][j] = 1/M
    for i in range(2,N+1):
        for j in range(1,M+1):
            for k in range(i,N*M+1):
                if k >= j:
                    dp[i][k] += dp[i-1][k-j]/M

    result = 0
    for i in range(N,N*M+1):
        result += dp[N][i]*max(1,i-K)
    print(result)