# 플로이드

n = int(input())    # 도시의 개수
m = int(input())    # 버스의 개수
inf = int(10**9)
graph = [[inf]*(n) for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1],c)

# Floyd-Warshall 알고리즘
for k in range(n):  # 거쳐가는 정점
    for i in range(n):  
        for j in range(n):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if i==j:
            print(0,end=' ')
        elif graph[i][j] == inf:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()