# Coordinates
# Gold 5, DFS

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,dx,dy = map(int,input().split())
    a,b = a-1,b-1
    graph[a].append((b,dx,dy))
    graph[b].append((a,-dx,-dy))

visited = [False]*N
visited[0] = True
q = [0]
result = [[0]*2 for _ in range(N)]
mx,my = 0,0
while q:
    x = q.pop()
    for nx,dx,dy in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            result[nx] = [result[x][0]+dx,result[x][1]+dy]
            mx = min(mx,result[nx][0])
            my = min(my,result[nx][1])
            q.append(nx)

for i in range(N):
    print(result[i][0]-mx,result[i][1]-my)