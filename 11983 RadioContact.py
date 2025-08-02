# Radio Contact
# Gold 1, DP

def f(a,b):
    return 10**9 if a < 0 or b < 0 else dp[a][b]

def dist(a,b):
    x1,y1 = pos[0][a]
    x2,y2 = pos[1][b]
    return (x1-x2)**2+(y1-y2)**2

N,M = map(int,input().split())
pos = [[tuple(map(int,input().split()))],[tuple(map(int,input().split()))]]
for i in range(2):
    for d in input():
        dx,dy = {'N':(0,1),'S':(0,-1),'W':(-1,0),'E':(1,0)}[d]
        x,y = pos[i][-1]
        pos[i].append((x+dx,y+dy))

dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(M+1):
        if i+j > 0:
            dp[i][j] = min(f(i-1,j),f(i,j-1),f(i-1,j-1))+dist(i,j)
print(dp[N][M])