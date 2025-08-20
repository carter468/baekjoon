# Canonical Coin Systems
# Gold 4, greedy, DP

N = int(input())
C = tuple(map(int,input().split()))

result = 'canonical'
m = sum(C[-2:])
dp = [10**9]*m
dp[0] = 0
for i in range(m):
    for c in C:
        if i >= c:
            dp[i] = min(dp[i],dp[i-c]+1)
        else:
            break

    g = 0
    x = i
    for j in range(N-1,-1,-1):
        g += x//C[j]
        x %= C[j]
        if x == 0: break
    if dp[i] < g:
        result = 'non-canonical'
        break
print(result)