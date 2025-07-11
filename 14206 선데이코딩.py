# 선데이 코딩
# Gold 2, DP, prefix sum

MOD = 10**9+7
R,S = map(int,input().split())

dp = [0]*(R*S+1)
dp[1] = 1
k = 1
for i in range(2,R+1):
    ndp = [0]*(R*S+1)
    for j in range(i,(i-1)*S+2):
        ndp[j] = (ndp[j-1]+dp[j-1])%MOD
    dp = ndp
    k = k*i%MOD

print(sum(dp)*k%MOD)