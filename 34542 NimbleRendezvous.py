# Nimble Rendezvous
# Gold 2, DP, math

A,B = map(int,input().split())

t = abs(A-B)
if t%2 == 1: exit(print(-1))

c = t.bit_length()-1
dp = [[0]*2 for _ in range(c+1)]
dp[0][0] = 1
for i in range(1,c):
    if t>>i&1 == 1:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][0]+dp[i-1][1]*2
    else:
        dp[i][0] = dp[i-1][0]*2+dp[i-1][1]
        dp[i][1] = dp[i-1][1]
print(c,dp[c-1][0])