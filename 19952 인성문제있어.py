# 인성 문제 있어??
# Gold 4, BFS

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    H,W,O,F,xs,ys,xe,ye = map(int,input().split())
    grid = [[0]*(W+1) for _ in range(H+1)]
    for _ in range(O):
        x,y,l = map(int,input().split())
        grid[x][y] = l

    visit = [[0]*(W+1) for _ in range(H+1)]
    visit[xs][ys] = 1
    q = deque([(xs,ys,F)])
    while q:
        x,y,f = q.popleft()
        if (x,y)==(xe,ye):
            print('잘했어!!')
            break
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx,y+dy
            if f>0 and 1<=nx<=H and 1<=ny<=W and visit[nx][ny]==0 and grid[nx][ny]-grid[x][y]<=f:
                q.append((nx,ny,f-1))
                visit[nx][ny] = 1
    else:
        print('인성 문제있어??')