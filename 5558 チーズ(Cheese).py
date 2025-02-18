# チーズ (Cheese)
# Gold 5, BFS

from collections import deque
import sys
input = sys.stdin.readline

def bfs(sx,sy,ex,ey):
    visited = [[-1]*W for _ in range(H)]
    visited[sx][sy] = 0
    q = deque([(sx,sy)])
    while q:
        x,y = q.popleft()
        if (x,y) == (ex,ey): return visited[x][y]
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == -1 and grid[nx][ny] != 'X':
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))

H,W,N = map(int,input().split())
grid = [input() for _ in range(H)]

arr = [0]*(N+1)
for i in range(H):
    for j in range(W):
        if grid[i][j].isdigit():
            arr[int(grid[i][j])] = i,j
        elif grid[i][j] == 'S':
            arr[0] = i,j

print(sum(bfs(*arr[i],*arr[i+1]) for i in range(N)))