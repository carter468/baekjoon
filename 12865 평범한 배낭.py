#평범한 배낭

# n,k = 6,17
# wv = [[6,13],[4,8],[1,3],[3,10],[5,5],[6,17]]
n,k = map(int,input().split())
wv = []
for _ in range(n):
    wv.append(list(map(int,input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    w = wv[i-1][0]
    v = wv[i-1][1]
    for j in range(1,k+1):
        if w>j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
    
print(dp[n][k])