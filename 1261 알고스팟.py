# 알고스팟
# Gold 4, 0-1 BFS

from collections import deque

m,n = map(int,input().split())
arr = [input() for _ in range(n)]

visited = [[-1]*m for _ in range(n)]
visited[0][0] = 0
q = deque([(0,0)])
while q:
    x,y = q.popleft()
    if (x,y) == (n-1,m-1):
        print(visited[x][y])
        break
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
            if arr[nx][ny] == '0':
                visited[nx][ny] = visited[x][y]
                q.appendleft((nx,ny))
            elif arr[nx][ny] == '1':
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))