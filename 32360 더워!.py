# 더워!
# Gold 2, BFS

from collections import deque

n,m = map(int,input().split())
K,C = map(int,input().split())
arr = [input() for _ in range(n)]

visited = [[100]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            q = deque([(i,j,0,0)])
            visited[i][j] = 0

while q:
    x,y,z,d = q.popleft()
    if arr[x][y] == 'E':
        print(d)
        break
    for nx,ny in (x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '#':
            if arr[nx][ny] in '.E':
                nz = z+C
                if nz < visited[nx][ny]:
                    visited[nx][ny] = nz
                    q.append((nx,ny,nz,d+1))
            else:
                nz = max(0,z-K)
                if nz < visited[nx][ny]:
                    visited[nx][ny] = nz
                    q.append((nx,ny,nz,d+1))
else: print(-1)
