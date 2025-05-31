# 아이템 먹기
# Gold 4, DP

def solve(x1,y1,x2,y2):
    dp = [[0]*111 for _ in range(111)]
    dp[x1][y1] = 1
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if not obs[i+1][j]: dp[i+1][j] += dp[i][j]
            if not obs[i][j+1]: dp[i][j+1] += dp[i][j]
    return dp[x2][y2]

N,M,A,B = map(int,input().split())
item = sorted([(1,1),(N,M)]+[tuple(map(int,input().split())) for _ in range(A)])
obs = [[False]*111 for _ in range(111)]
for _ in range(B):
    x,y = map(int,input().split())
    obs[x][y] = True

result = 1
for i in range(A+1):
    result *= solve(*item[i],*item[i+1])
print(result)