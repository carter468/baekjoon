# Iguana Instructions
# Gold 4, BFS

from collections import deque

n = int(input())
arr = [input() for _ in range(n)]

q = deque([(0,0)])
visited = [[-1]*n for _ in range(n)]
visited[0][0] = 0
while q:
    x,y = q.popleft()
    if (x,y) == (n-1,n-1): break
    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        nx,ny = x+dx,y+dy
        while 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == '.':
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
            nx += dx
            ny += dy
print(visited[x][y])
