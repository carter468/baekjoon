# 벽 타기
# Gold 3, 0-1 BFS

from collections import deque

h,w = map(int,input().split())
grid = [list(input()) for _ in range(h)]

distance = [[10**9]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'S':
            q = deque([(i,j)])
            distance[i][j] = 0
        elif grid[i][j] == 'E':
            ex,ey = i,j
        if grid[i][j] != '#':
            for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if grid[x][y] == '#':
                    grid[i][j] = '-'
                    break

while q:
    x,y = q.popleft()

    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != '#':
            if grid[x][y] == '-' and grid[nx][ny] == '-':
                if distance[nx][ny] > distance[x][y]:
                    distance[nx][ny] = distance[x][y]
                    q.appendleft((nx,ny))
            else:
                if distance[nx][ny] > distance[x][y]+1:
                    distance[nx][ny] = distance[x][y]+1
                    q.append((nx,ny))

print(distance[ex][ey])