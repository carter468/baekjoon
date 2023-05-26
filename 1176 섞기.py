# 섞기
# Gold 1, DP_bitfield

n,m = map(int,input().split())
height = []
dp = [[0]*n for _ in range(1<<n)]
for i in range(n):
    height.append(int(input()))
    dp[1<<i][i] = 1

for i in range(1<<n):
    for j in range(n):
        if dp[i][j] == 0: continue
        for k in range(n):
            if i&(1<<k) == 0 and abs(height[j]-height[k]) > m:
                dp[i|(1<<k)][k] += dp[i][j]

print(sum(dp[-1]))