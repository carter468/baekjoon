# Labyrinth
# Gold 2, BFS

from collections import deque
import sys
input = sys.stdin.readline

def f():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.': return i,j

for _ in range(int(input())):
    m,n = map(int,input().split())
    grid = [input() for _ in range(n)]

    x,y = f()
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))

    visited = [[-1]*m for _ in range(n)]
    visited[x][y] = 0
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
    print(f'Maximum rope length is {visited[x][y]}.')