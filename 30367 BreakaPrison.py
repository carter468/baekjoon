# Break a Prison
# Gold 3, BFS

from collections import deque
D = (0,1),(1,0),(0,-1),(-1,0)

N,M = map(int,input().split())
grid = [input() for _ in range(N)]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'S':
            q = deque([(i,j,None)])

visited = [[[-1]*4 for _ in range(M)] for _ in range(N)]
while q:
    x,y,d = q.popleft()
    if grid[x][y] == 'E':
        print(visited[x][y][d])
        break

    s = {0,1,2,3}
    if d != None: s.remove((d+1)%4)
    for nd in s:
        dx,dy = D[nd]
        nx,ny = x+dx,y+dy
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '#' and visited[nx][ny][nd] == -1:
            if d == None:
                visited[nx][ny][nd] = 1
            else:
                visited[nx][ny][nd] = visited[x][y][d]+1
            q.append((nx,ny,nd))

else: print(-1)