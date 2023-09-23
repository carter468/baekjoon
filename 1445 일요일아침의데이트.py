# 일요일 아침의 데이트
# Gold 2, dijkstra

import heapq

n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            sx,sy = i,j
        elif grid[i][j] == 'F':
            fx,fy = i,j
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'g':
            for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0 <= x < n and 0 <= y < m and grid[x][y] == '.':
                    grid[x][y] = 'h'

q = [(0,0,sx,sy,set([(sx,sy)]))]
while 1:
    a,b,x,y,visit = heapq.heappop(q)
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if (nx,ny) == (fx,fy):
            print(a,b)
            exit()
        if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in visit:
            visit.add((nx,ny))
            if grid[nx][ny] in '.S':
                heapq.heappush(q,(a,b,nx,ny,visit))
            elif grid[nx][ny] == 'g':
                heapq.heappush(q,(a+1,b,nx,ny,visit))
            elif grid[nx][ny] == 'h':
                heapq.heappush(q,(a,b+1,nx,ny,visit))