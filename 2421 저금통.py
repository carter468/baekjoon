# 저금통
# Gold 5, DP

seive = [1]*10**6
for i in range(2,10**3):
    if seive[i]:
        for j in range(i*i,10**6,i):
            seive[j] = 0

dp = [[0]*1000 for _ in range(1000)]
for i in range(1,1000):
    for j in range(1,1000):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])+seive[int(str(i)+str(j))]

n = int(input())
print(dp[n][n]-1)