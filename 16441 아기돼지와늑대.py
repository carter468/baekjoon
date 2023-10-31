# 아기돼지와 늑대
# Gold 3, DFS

n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]

q = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'W': q.append((i,j))

visited = [[False]*m for _ in range(n)]
while q:
    x,y = q.pop()
    
    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        nx,ny = x+dx,y+dy
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
            if grid[nx][ny] == '.':
                visited[nx][ny] = True
                q.append((nx,ny))
            elif grid[nx][ny] == '+':
                while grid[nx][ny] == '+':
                    nx += dx
                    ny += dy
                if grid[nx][ny] == '.' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                elif grid[nx][ny] == '#' and visited[nx-dx][ny-dy] == False:
                    visited[nx-dx][ny-dy] = True
                    q.append((nx-dx,ny-dy))

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' and visited[i][j] == False:
            grid[i][j] = 'P'

for g in grid:
    print(''.join(g))