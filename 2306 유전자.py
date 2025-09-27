# 유전자
# Gold 3, DP

S = input()

n = len(S)
dp = [[0]*n for _ in range(n)]
for length in range(2,n+1):
    for l in range(n-length+1):
        r = l+length-1
        dp[l][r] = max(dp[l][m]+dp[m+1][r] for m in range(l,r))
        if S[l]+S[r] in ('at','gc'):
            dp[l][r] = max(dp[l][r],dp[l+1][r-1]+2)
print(dp[0][-1])