# Meteor Shower
# Gold 3, BFS

from collections import deque
import sys
input = sys.stdin.readline
M = 305

grid = [[1001]*M for _ in range(M)]
for _ in range(int(input())):
    x,y,t = map(int,input().split())
    for nx,ny in (x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1):
        grid[nx][ny] = min(grid[nx][ny],t)

visited = [[-1]*M for _ in range(M)]
visited[0][0] = 0
q = deque([(0,0)])
while q:
    x,y = q.popleft()
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < M and 0 <= ny < M and visited[nx][ny] == -1:
            if grid[nx][ny] == 1001:
                print(visited[x][y]+1)
                exit()
            if visited[x][y]+1 < grid[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
print(-1)