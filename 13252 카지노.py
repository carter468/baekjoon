# 카지노
# Gold 3, DP, greedy

from collections import defaultdict

N,M,K = map(int,input().split())

dp = {N:1}
for _ in range(K):
    ndp = defaultdict(int)
    for n in dp:
        a,b = divmod(n,M)
        if n-a > 0:
            ndp[n-a] += dp[n]*(M-b)/M
        if b > 0 and n-a-1 > 0:
            ndp[n-a-1] += dp[n]*b/M
    dp = ndp

print(sum(dp.values()))