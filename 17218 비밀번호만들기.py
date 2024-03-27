# 비밀번호 만들기
# Gold 4, DP, LCS

a,b = input(),input()

la,lb = len(a),len(b)
dp = [[0]*(lb+1) for _ in range(la+1)]
for i in range(la):
    for j in range(lb):
        if a[i] == b[j]: dp[i+1][j+1] = dp[i][j]+1
        else: dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

result = []
while dp[la][lb] > 0:
    if dp[la][lb] == dp[la-1][lb]:
        la -= 1
    elif dp[la][lb] == dp[la][lb-1]:
        lb -= 1
    else:
        result.append(a[la-1])
        la -= 1
        lb -= 1
print(''.join(result[::-1]))