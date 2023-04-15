# 소수 화폐
# Gold 5, DP

n = int(input())

seive = [1]*(n+1)
for i in range(2,int(n**0.5)+1):
    if seive[i]:
        for j in range(i*i,n+1,i):
            seive[j] = 0

dp = [1]+[0]*n
for i in range(2,n+1):
    if seive[i]:
        for j in range(i,n+1):
            dp[j] = (dp[j]+dp[j-i])%123456789

print(dp[n])