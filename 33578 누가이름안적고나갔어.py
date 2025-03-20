# 누가 이름 안 적고 나갔어
# Gold 4, BFS

from collections import deque
import sys
input = sys.stdin.readline
INF = 10**9

def bfs(i,j):
    dist = [[-1]*M for _ in range(N)]
    dist[i][j] = 0
    q = deque([(i,j)])
    while q:
        x,y = q.popleft()
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '#' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y]+1
                q.append((nx,ny))
    return dist

N,M = map(int,input().split())
grid = [input() for _ in range(N)]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'J': dist1 = bfs(i,j)
        elif grid[i][j] == 'S': dist2 = bfs(i,j)
    
result = INF
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'S' and dist1[i][j] != -1: result = min(result,dist1[i][j]*2)
        elif grid[i][j] == 'T' and dist1[i][j] != -1 and dist2[i][j] != -1: result = min(result,dist1[i][j]*2+dist2[i][j])
print(result if result != INF else -1)