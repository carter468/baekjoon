# 직사각형 탈출
# Gold 4, 너비 우선 탐색

from collections import deque
import sys
input = sys.stdin.readline

def check():
    if dy==0:
        if dx==-1:
            if 1 in grid[nx][ny:ny+W]:
                return False
        else:
            if 1 in grid[nx+H-1][ny:ny+W]:
                return False
    else:
        if dy==-1:
            for i in range(H):
                if grid[nx+i][ny] == 1:
                    return False
        else:
            for i in range(H):
                if grid[nx+i][ny+W-1] == 1:
                    return False
    return True
                        
N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
H,W,sr,sc,fr,fc = map(int,input().split())

q = deque([(sr-1,sc-1)])
grid[sr-1][sc-1] = -1
while q:
    x,y = q.popleft()
    if (x,y)==(fr-1,fc-1):
        print(-grid[x][y]-1)
        break

    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx,ny = x+dx,y+dy
        if 0<=nx<=N-H and 0<=ny<=M-W and grid[nx][ny]==0:
            grid[nx][ny] = grid[x][y] - 1
            if check():
                q.append((nx,ny))
else:
    print(-1)