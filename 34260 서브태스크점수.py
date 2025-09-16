# 서브태스크 점수
# Gold 1, DP, bitmask, bruteforcing

import sys
input = sys.stdin.readline
MOD = 998244353

P = int(input())
dp = [[0]*(P*100+1) for _ in range(P+1)]
dp[0][0] = 1
for p in range(1,P+1):
    N,M = map(int,input().split())
    S = tuple(map(int,input().split()))
    R = [tuple(map(int,input().split())) for _ in range(M)]

    for i in range(1<<N):
        a = bin(i)[2:].rjust(N,'0')
        for x,y in R:
            if a[x-1] == '0' and a[y-1] == '1':
                break
        else:
            s = 0
            for j in range(N):
                if a[j] == '1':
                    s += S[j]
            for j in range((p-1)*100+1):
                dp[p][j+s] = (dp[p][j+s]+dp[p-1][j])%MOD

result = 0
for i in range(P*100+1):
    result = (result+dp[P][i]*i)%MOD
print(result)