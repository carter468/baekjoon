# 파스타
# Gold 4, DP

M = 10000

n,k = map(int,input().split())
arr = [0]*(n+1)
for _ in range(k):
    a,b = map(int,input().split())
    arr[a] = b

dp = [[0]*6 for _ in range(n+1)]
if arr[1]: dp[1][arr[1]-1] = 1
else: dp[1] = [1,1,1,0,0,0]

for i in range(2,n+1):
    if arr[i]: j = [arr[i]-1]
    else: j = [0,1,2]
    for k in j:
        dp[i][k] = (dp[i-1][(k+1)%3]+dp[i-1][(k+1)%3+3]+dp[i-1][(k+2)%3]+dp[i-1][(k+2)%3+3])%M
        dp[i][k+3] = dp[i-1][k]

print(sum(dp[n])%M)