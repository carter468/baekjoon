# Change Making
# Gold 5, DP, greedy

input()
arr = tuple(map(int,input().split()))

dp = [0]+[10**9]*100000
g = [0]

for i in range(1,100001):
    t = 1
    for c in arr:
        if c <= i:
            dp[i] = min(dp[i],dp[i-c]+1)
            t = c
    g.append(g[i-t]+1)
    
    if dp[i] != g[i]:
        exit(print(i))

print(-1)