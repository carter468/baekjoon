# 백룸
# Gold 4, DP

n,m = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]
x1,y1,x2,y2 = map(int,input().split())
if x1 == x2 and y1 > y2: y1,y2 = y2,y1
if y1 == y2 and x1 > x2: x1,x2 = x2,x1

dp = [[-10**10]*m for _ in range(n)]
dp[0][0] = arr[0][0]
for i in range(n):
    for j in range(m):
        if not (x1 == x2 == i and y1 <= j < y2): dp[i][j] = max(dp[i][j],dp[i-1][j]+arr[i][j])
        if not (y1 == y2 == j and x1 <= i < x2): dp[i][j] = max(dp[i][j],dp[i][j-1]+arr[i][j])
print(dp[-1][-1] if dp[-1][-1] > -10**7 else 'Entity')
