# 공통 부분 문자열
# Gold 5, DP

a,b = input(),input()

result = 0
dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[i+1][j+1] = dp[i][j]+1
        result = max(result,dp[i+1][j+1])
print(result)