# 미로 만들기
# Gold 4, 0-1 BFS

from collections import deque

N = int(input())
grid = [input() for _ in range(N)]

visited = [[-1]*N for _ in range(N)]
visited[0][0] = 0
q = deque([(0,0)])
while q:
    x,y = q.popleft()
    if (x,y) == (N-1,N-1): break

    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
            if grid[nx][ny] == '0':
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
            else:
                visited[nx][ny] = visited[x][y]
                q.appendleft((nx,ny))

print(visited[-1][-1])