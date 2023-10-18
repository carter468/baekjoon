# 두 부분 문자열
# Gold 4, LCS

a,b = input(),input()
l1,l2 = len(a),len(b)

dp = [[0]*(l2+1) for _ in range(l1+1)]
for i in range(1,l1+1):
    for j in range(1,l2+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

print(l1+l2-dp[-1][-1])