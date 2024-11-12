# Escape Room
# Gold 2, DFS

N,M = int(input()),int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]

graph = [[] for _ in range(10**6+1)]
for i in range(N):
    for j in range(M):
        graph[arr[i][j]].append((i+1,j+1))

visited = [[False]*(M+1) for _ in range(N+1)]
visited[N][M] = True
q = [(N,M)]
while q:
    x,y = q.pop()
    if (x,y) == (1,1):
        print('yes')
        break

    for nx,ny in graph[x*y]:
        if not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx,ny))
else: print('no')