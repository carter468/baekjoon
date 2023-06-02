# Cow Beauty Pageant
# Gold 5, BFS, DFS

from collections import deque
import sys
input = sys.stdin.readline
M = 5931
sys.setrecursionlimit(M)

def dfs(x,y):
    grid[x][y] = k
    for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 'X':
            dfs(nx,ny)

def bfs(i,j):
    q = deque([(i,j)])
    visit = [[-2]*m for _ in range(n)]
    visit[i][j] += 1
    while q:
        x,y = q.popleft()
        if grid[i][j]*grid[x][y] < 0:
            return visit[x][y]
        for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != grid[i][j] and visit[nx][ny] == -2:
                q.append((nx,ny))
                visit[nx][ny] = visit[x][y]+1
    return M

n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]

k = -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'X':
            dfs(i,j)
            k = 1
        elif grid[i][j] == '.':
            grid[i][j] = 0

result = M
for i in range(n):
    for j in range(m):
        if grid[i][j] != 0:
            result = min(result,bfs(i,j))
print(result)