# Maze Connect
# Gold 2, DFS, implementation

import sys
input = sys.stdin.readline

def dfs(i,j,k):
    result = 1
    visited[i][j][k] = True
    q = [(i,j,k)]
    while q:
        x,y,z = q.pop()
        if maze[x][y] == '.':
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                nx,ny = x+dx,y+dy
                if nx < 0 or nx == R or ny < 0 or ny == C:
                    result = 0
                    continue
                if maze[nx][ny] == '.':
                    nz = 0
                elif maze[nx][ny] == '/':
                    nz = 0 if dx+dy == 1 else 1
                else:
                    nz = 0 if dx == -1 or dy == 1 else 1
                if not visited[nx][ny][nz]:
                    visited[nx][ny][nz] = True
                    q.append((nx,ny,nz))
        else:
            if maze[x][y] == '/':
                if z == 0:
                    arr = (-1,0,0),(0,-1,1)
                else:
                    arr = (1,0,1),(0,1,0)
            else:
                if z == 0:
                    arr = (1,0,0),(0,-1,1)
                else:
                    arr = (-1,0,1),(0,1,0)
            for dx,dy,nz in arr:
                nx,ny = x+dx,y+dy
                if nx < 0 or nx == R or ny < 0 or ny == C:
                    result = 0
                    continue
                if maze[nx][ny] == '.':
                    nz = 0
                if not visited[nx][ny][nz]:
                    visited[nx][ny][nz] = True
                    q.append((nx,ny,nz))
    return result

R,C = map(int,input().split())
maze = [input() for _ in range(R)]

count = 0
visited = [[[False]*2 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if not visited[i][j][0]:
            count += dfs(i,j,0)
        if maze[i][j] != '.' and not visited[i][j][1]:
            count += dfs(i,j,1)
print(count)