# N중 슬릿 실험
# Platinum 5, DP

INF = 10**15

def check(i,j,a,b):
    x1 = slit[j][b]
    x2 = slit[i][a]

    for k in range(j+1,i):
        l,r = slit[k]
        x3 = (k-j)*(x1-x2)/(j-i)+x1
        if x3 < l or r < x3: return INF
        
    return ((i-j)**2+(x1-x2)**2)**0.5

M,N = map(int,input().split())
slit = [(0,0)]+[tuple(map(int,input().split())) for _ in range(N)]+[(0,0)]

dp = [[INF]*2 for _ in range(N+2)]
dp[0] = [0,0]

for i in range(1,N+2):
    for j in range(i):
        for a,b in (0,0),(0,1),(1,0),(1,1):
            dp[i][a] = min(dp[i][a],dp[j][b]+check(i,j,a,b))

print(dp[-1][0])