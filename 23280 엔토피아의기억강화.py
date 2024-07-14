# 엔토피아의 기억강화
# Gold 3, DP

def dist(x,y):
    xa,xb = divmod(x,3)
    ya,yb = divmod(y,3)
    return abs(xa-ya)+abs(xb-yb)

n,a,b = map(int,input().split())
arr = tuple(map(int,input().split()))

dp = [[[10**9]*12 for _ in range(12)] for _ in range(n+1)]
dp[0][0][2] = 0
for i in range(1,n+1):
    p = arr[i-1]-1
    for j in range(12):
        for k in range(12):
            dp[i][p][k] = min(dp[i][p][k],dp[i-1][j][k]+dist(j,p)+a)
            dp[i][j][p] = min(dp[i][j][p],dp[i-1][j][k]+dist(k,p)+b)

result = 10**9
for i in range(12):
    for j in range(12):
        result = min(result,dp[-1][i][j])
print(result)