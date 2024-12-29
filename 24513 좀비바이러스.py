# 좀비 바이러스
# Gold 3, BFS

from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            a,b = i,j
        if arr[i][j] == 2:
            c,d = i,j

visited = [[-1]*M for _ in range(N)]
visited[a][b] = [0,0]
visited[c][d] = [0,1]
q = deque([(a,b,0),(c,d,1)])
while q:
    x,y,z = q.popleft()
    if visited[x][y][1] != z: continue
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != -1:
            if visited[nx][ny] == -1:
                visited[nx][ny] = [visited[x][y][0]+1,z]
                q.append((nx,ny,z))
            elif visited[nx][ny][0] == visited[x][y][0]+1 and visited[nx][ny][1] != z:
                visited[nx][ny][1] = 2

count = [0]*3
for i in range(N):
    for j in range(M):
        if visited[i][j] != -1:
            count[visited[i][j][1]] += 1
print(*count)