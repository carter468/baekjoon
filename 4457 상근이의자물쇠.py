# 상근이의 자물쇠
# Gold 2, DP

M = 18
MOD = 10**9

def solve(h,n):
    if h == -1: return n == 0
    if h == -2 or n == 0: return 0
    if dp[h][n] != -1: return dp[h][n]
    dp[h][n] = 0
    for i in range(n):
        dp[h][n] = (dp[h][n]+solve(h-1,i)*solve(h-1,n-1-i)+solve(h-1,i)*solve(h-2,n-1-i)+solve(h-2,i)*solve(h-1,n-1-i))%MOD
    return dp[h][n]

dp = [[-1]*1428 for _ in range(M)]
while True:
    try:
        N = int(input())
    except:
        break

    result = 0
    for H in range(M):
        result = (result+solve(H,N))%MOD
    print(format(result,"09"))