# 격자의 분리자
# Gold 5, BFS

from collections import deque

while True:
    n,m = map(int,input().split())
    if n == 0: break
    arr = [list(input()) for _ in range(n)]
    
    visited = [[0]*m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if i == 0 and arr[i][j] == 'S':
                q.append((i,j))
                visited[i][j] = 1
            elif arr[i][j] == 'B':
                arr[i][j] = 'S'
                if i == 0:
                    q.append((i,j))
                    visited[i][j] = 1
                break
    
    while q:
        x,y = q.popleft()
        if x == n-1:
            print(visited[x][y])
            break

        for nx,ny in (x+1,y),(x,y+1),(x,y-1):
            if 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] == 'S':
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))