# 숫자카드
# Gold 5, DP

s = input()

l = len(s)+1
dp = [0]*l
dp[0] = 1
if s[0] != '0': dp[1] = 1
for i in range(2,l):
    if s[i-1] != '0': 
        dp[i] = dp[i-1]
    if s[i-2] != '0' and int(s[i-2:i]) <= 34:
        dp[i] += dp[i-2]
print(dp[-1])