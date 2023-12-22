# 최소 편집
# Gold 3, DP, LCS

a,b = input(),input()
la,lb = len(a),len(b)

dp = [[0]*(lb+1) for _ in range(la+1)]
for i in range(la+1):
    dp[i][0] = i
for j in range(lb+1):
    dp[0][j] = j

for i in range(1,la+1):
    for j in range(1,lb+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1

print(dp[-1][-1])