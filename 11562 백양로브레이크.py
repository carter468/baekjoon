# 11562 백양로 브레이크
# Gold 3, floyd-warshall

n,m = map(int,input().split())
graph = [[999]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u,v,b = map(int,input().split())
    graph[u][v] = 0
    graph[v][u] = 0 if b == 1 else 1

for k in range(1,n+1):
    graph[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for _ in range(int(input())):
    s,e = map(int,input().split())
    print(graph[s][e])