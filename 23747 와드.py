# 와드
# Gold 5, simultaion, BFS

import sys
input = sys.stdin.readline

r,c = map(int,input().split())
grid = [input() for _ in range(r)]
x,y = map(int,input().split())
x,y = x-1,y-1

result = [['#']*c for _ in range(r)]
for a in list(input().strip()):
    if a == 'W':
        if result[x][y] == '#':
            result[x][y] = '.'
            q = [(x,y)]
            while q:
                i,j = q.pop()
                for ni,nj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == grid[x][y] and result[ni][nj] == '#':
                        result[ni][nj] = '.'
                        q.append((ni,nj))
    else:
        dx,dy = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}[a]
        x += dx
        y += dy

for nx,ny in (x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1):
    if 0 <= nx < r and 0 <= ny < c:
        result[nx][ny] = '.'
for a in result:
    print(''.join(a))