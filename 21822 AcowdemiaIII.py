# Acowdemia III
# Gold 3, greedy

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
grid = [list(input()) for _ in range(N)]

count = 0
v = set()
for x in range(N):
    for y in range(M):
        if grid[x][y] == 'G':
            for dx,dy in (0,1),(1,0):
                c = 0
                for nx,ny in (x+dx,y+dy),(x-dx,y-dy):
                    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 'C':
                        c += 1
                if c == 2:
                    count += 1
                    grid[x][y] = '.'
                    break

        if grid[x][y] == 'G':
            for nx,ny in (x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1):
                if 0 <= nx < N and 0 <= ny < M and grid[nx][y] == 'C' and grid[x][ny] == 'C':
                    a,b,c,d = nx,y,x,ny
                    if a > c: a,b,c,d = c,d,a,b
                    if (a,b,c,d) not in v:
                        v.add((a,b,c,d))
                        count += 1
                        grid[x][y] = '.'
                        break

print(count)