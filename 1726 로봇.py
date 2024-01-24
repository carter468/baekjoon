# 로봇
# Gold 3, BFS

from collections import deque

m,n = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(m)]
sx,sy,sd = map(int,input().split())
ex,ey,ed = map(int,input().split())

sx,sy,sd = sx-1,sy-1,(0,2,1,3)[sd-1]
ex,ey,ed = ex-1,ey-1,(0,2,1,3)[ed-1]
visited = [[[-1]*4 for _ in range(n)] for _ in range(m)]
visited[sx][sy][sd] = 0
q = deque([(sx,sy,sd)])
while q:
    x,y,d = q.popleft()
    if (x,y,d) == (ex,ey,ed):
        print(visited[x][y][d])
        break

    for t in (1,-1):
        nd = (d+t)%4
        if visited[x][y][nd] == -1:
            visited[x][y][nd] = visited[x][y][d]+1
            q.append((x,y,nd))

    dx,dy = [(0,1),(1,0),(0,-1),(-1,0)][d]
    for k in (1,2,3):
        nx,ny = x+dx*k,y+dy*k
        if nx < 0 or nx == m or ny < 0 or ny == n or arr[nx][ny] == 1: break
        if visited[nx][ny][d] == -1:
            visited[nx][ny][d] = visited[x][y][d]+1
            q.append((nx,ny,d))