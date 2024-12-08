# 벽 부수고 이동하기 3
# Gold 1, BFS

from collections import deque
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
grid = [input() for _ in range(N)]

visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
q = deque([(0,0,1,0)])
while q:
    x,y,d,c = q.popleft()
    if (x,y) == (N-1,M-1):
        print(d)
        break
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == '0' and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = 1
                q.append((nx,ny,d+1,c))
            elif grid[nx][ny] == '1' and c < K and visited[nx][ny][c+1] == 0:
                if d%2 == 1:
                    visited[nx][ny][c+1] = 1
                    q.append((nx,ny,d+1,c+1))
                else:
                    q.append((x,y,d+1,c))
else: print(-1)