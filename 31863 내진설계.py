# 내진 설계
# Gold 5, BFS

from collections import deque

n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            x,y = i,j
            grid[i][j] = '.'
        elif grid[i][j] == '#':
            grid[i][j] = 2
            count += 1
        elif grid[i][j] == '*':
            grid[i][j] = 1
            count += 1

count1 = 0
q = deque()
arr = []
for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
    nx,ny = x+dx,y+dy
    if 0 <= nx < n and 0 <= ny < m:
        if grid[nx][ny] != '|':
            arr.append((nx+dx,ny+dy))
        if grid[nx][ny] == 1:
            q.append((nx,ny))
            count1 += 1
            grid[nx][ny] = '.'
        elif grid[nx][ny] == 2:
            grid[nx][ny] = 1
for nx,ny in arr:
    if 0 <= nx < n and 0 <= ny < m:
        if grid[nx][ny] == 1:
            q.append((nx,ny))
            count1 += 1
            grid[nx][ny] = '.'
        elif grid[nx][ny] == 2:
            grid[nx][ny] = 1

while q:
    x,y = q.popleft()
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 1:
                q.append((nx,ny))
                count1 += 1
                grid[nx][ny] = '.'
            elif grid[nx][ny] == 2:
                grid[nx][ny] = 1

print(count1,count-count1)