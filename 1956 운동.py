# 운동
import sys
input = sys.stdin.readline

v,e = map(int,input().split())

inf = int(10**9)
graph = [[inf]*(v) for _ in range(v)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = c

# 플로이드 와샬 알고리즘
for k in range(v):  # 거쳐가는 정점
    for i in range(v):  
        for j in range(v):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

ans = inf

for i in range(v):
    ans = min(ans,graph[i][i])

if ans == inf:
    print(-1)
else:
    print(ans)