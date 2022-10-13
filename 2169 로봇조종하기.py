# 로봇 조종하기

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
value = []
for _ in range(n):
    value.append(tuple(map(int,input().split())))
dp = [[-10**6 for _ in range(m)] for _ in range(n)]
dp[0][0] = value[0][0]
visit = [[[] for _ in range(m)] for _ in range(n)]
visit[0][0] = [[0,0]]
dx = [-1,1,0]
dy = [0,0,1]
for i in range(n):
    for j in range(m):
        for k in range(3):
            x = i+dx[k]
            y = j+dy[k]
            if x<0 or x>n-1 or y<0 or y>m-1 or [x,y] in visit[i][j]:
                continue
            tmp = dp[i][j] + value[x][y]
            if tmp > dp[x][y]:
                dp[x][y] = tmp
                visit[x][y] = visit[i][j]+[[x,y]]
print(dp[n-1][m-1])

# 10   25    7  8   13
# 68   24  -78  63  32
# 12  -69  100 -29 -25
# -16 -22  -57 -33  99
# 7   -76  -11  77  15