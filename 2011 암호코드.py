# 암호코드
# Gold 5, DP

n = list(map(int,input()))

dp = [0]*(len(n)+1)
dp[0],dp[1] = 1,1
if n[0] == 0: print(0)
else:
    for i in range(1,len(n)):
        if n[i] > 0:
            dp[i+1] += dp[i]
        if 10 <= n[i]+n[i-1]*10 <= 26:
            dp[i+1] += dp[i-1]
    print(dp[-1]%1000000)
