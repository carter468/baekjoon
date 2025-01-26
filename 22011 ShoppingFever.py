# Shopping Fever
# Gold 4, DP

n,q = map(int,input().split())
p = sorted(map(int,input().split()),reverse=True)

q = 100-q
dp = [0]*n
for i in range(n):
    if i < 2:
        dp[i] = dp[i-1]+p[i]*q//100
    else:
        dp[i] = min(dp[i-1]+p[i]*q//100,dp[i-3]+p[i-2]+p[i-1])
print(dp[-1])