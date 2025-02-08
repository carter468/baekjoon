# Brackets
# Gold 3, DP

while (s:=input()) != 'end':
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if s[i]+s[j] in ('()','[]'):
                dp[i][j] = max(dp[i][j],dp[i+1][j-1]+2)
            for k in range(i,j):
                dp[i][j] = max(dp[i][j],dp[i][k]+dp[k+1][j])
    print(dp[0][-1])