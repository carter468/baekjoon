# No Left Turns
# Gold 3, BFS

from collections import deque
import sys
input = sys.stdin.readline
D = (0,1),(1,0),(0,-1),(-1,0)

for _ in range(int(input())):
    r,c = map(int,input().split())
    grid = [input() for _ in range(r)]

    visited = [[[-1]*4 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'S':
                q = deque([(i,j,k) for k in range(4)])
                visited[i][j] = [0]*4

    while True:
        x,y,d = q.popleft()
        if grid[x][y] == 'F':
            print(visited[x][y][d])
            break
        
        for nd in (d,(d+1)%4):
            nx,ny = x+D[nd][0],y+D[nd][1]
            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] != 'X' and visited[nx][ny][nd] == -1:
                visited[nx][ny][nd] = visited[x][y][d]+1
                q.append((nx,ny,nd))