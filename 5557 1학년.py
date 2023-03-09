# 1학년
# Gold 5, dp

input()
n = tuple(map(int,input().split()))

dp = [0]*30
dp[n[0]] = 1
for x in n[1:-1]:
    dp_ = [0]*30
    for i in range(21):
        dp_[i+x] += dp[i]
        dp_[i-x] += dp[i]
    dp = dp_
print(dp[n[-1]])