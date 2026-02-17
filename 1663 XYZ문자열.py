# XYZ 문자열
# Gold 2, DP

Q = int(input())
N = int(input())

dp = [[0,0,0] for _ in range(N+1)]
dp[1][0] = 1
for i in range(2,N+1):
    dp[i] = [dp[i-1][2],dp[i-1][0],dp[i-1][0]+dp[i-1][1]]

if Q == 1: print(sum(dp[N]))
elif Q == 3: print(dp[N][ord(input())-88])
else:
    k = int(input())
    while N > 3:
        if k <= sum(dp[N-3]):
            N -= 3
        else:
            k -= sum(dp[N-3])
            N -= 2
    print(['X','YZ','ZX'][N-1][k-1])