# 보물섬
# Gold 5, BFS, bruteforcing

from collections import deque

def bfs(x,y):
    visited = [[-1]*M for _ in range(N)]
    visited[x][y] = 0
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 'L' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
    return visited[x][y]

N,M = map(int,input().split())
arr = [input() for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            result = max(result,bfs(i,j))
print(result)