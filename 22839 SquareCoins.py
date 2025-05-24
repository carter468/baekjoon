# Square Coins
# Gold 5, DP

dp = [1]+[0]*300
for i in range(1,18):
    for j in range(i*i,301):
        dp[j] += dp[j-i*i]
        
while n:=int(input()):
    print(dp[n])