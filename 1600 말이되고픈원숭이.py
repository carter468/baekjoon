# 말이 되고픈 원숭이
# Gold 3, BFS

from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
w,h = map(int,input().split())
grid = [tuple(input().split()) for _ in range(h)]
visit = [[[-1]*(k+1) for _ in range(w)] for _ in range(h)]

q = deque([(0,0,0)])
visit[0][0][0] = 0
while q:
    x,y,c = q.popleft()

    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx,ny = x+dx,y+dy
        if 0<=nx<h and 0<=ny<w and grid[nx][ny]=='0' and visit[nx][ny][c]==-1:
            visit[nx][ny][c] = visit[x][y][c]+1
            q.append((nx,ny,c))

    if c==k: continue
    for dx,dy in ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)):
        nx,ny = x+dx,y+dy
        if 0<=nx<h and 0<=ny<w and grid[nx][ny]=='0' and visit[nx][ny][c+1]==-1:
            visit[nx][ny][c+1] = visit[x][y][c]+1
            q.append((nx,ny,c+1))

answer = 10**5
for i in range(k+1):
    if visit[h-1][w-1][i] == -1: continue
    answer = min(answer,visit[h-1][w-1][i])
print(answer if answer!=10**5 else -1)