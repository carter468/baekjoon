# 조교의 맹연습
# Gold 4, DP

INF = 10**9

a,b,c,k = map(int,input().split())

dp = [[INF]*4 for _ in range(k+1)]
dp[0][0] = 0

for i in range(k):
    for j in range(4):
        for cost,d in (a,-1),(b,1),(c,2):
            ni,nj = i+cost,(j+d)%4
            if ni > k: continue
            dp[ni][nj] = min(dp[ni][nj],dp[i][j]+1)

print(dp[k][0] if dp[k][0] != INF else -1)