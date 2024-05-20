# 허들 넘기
# Gold 3, floyd-warshall

n,m,t = map(int,input().split())
height = [[10**9]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u,v,h = map(int,input().split())
    height[u][v] = min(height[u][v],h)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            height[i][j] = min(height[i][j],max(height[i][k],height[k][j]))

for _ in range(t):
    s,e = map(int,input().split())
    print(height[s][e] if height[s][e] != 10**9 else -1)