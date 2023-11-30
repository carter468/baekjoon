# 거울 설치
# Gold 3, BFS

from collections import deque

D = [((-1,0),(1,0)),((0,-1),(0,1))]

n = int(input())
arr = [input() for _ in range(n)]

door = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '#': door.append((i,j))
sx,sy = door[0]

visited = [[[-1]*2 for _ in range(n)] for _ in range(n)]
visited[sx][sy] = [0,0]
q = deque([(sx,sy,0),(sx,sy,1)])
while True:
    x,y,d = q.popleft()

    for dx,dy in D[d]:
        nx,ny = x+dx,y+dy
        while 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != '*':
            if (nx,ny) == door[1]:
                print(visited[x][y][d])
                exit()
            
            if arr[nx][ny] == '!' and visited[nx][ny][d^1] == -1:
                visited[nx][ny][d^1] = visited[x][y][d]+1
                q.append((nx,ny,d^1))
            nx += dx
            ny += dy