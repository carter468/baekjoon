# gmb 수열
# Platinum 3, DP

MOD = 10**9+7
MAX = 300

N = int(input())
B = tuple(map(int,input().split()))

dp = [[0]*MAX for _ in range(MAX)]
dp1 = [0]*MAX
dp2 = [[0]*MAX for _ in range(MAX)]

for b in B:
    for i in range(b,MAX):
        j = i-b
        dp[j][b] = (dp[j][b]+dp[i][j]+dp2[i][j])%MOD
        dp2[i][b] = (dp2[i][b]+dp1[i])%MOD
    dp1[b] += 1

result = 0
for i in range(MAX):
    for j in range(MAX):
        result = (result+dp[i][j])%MOD
print(result)