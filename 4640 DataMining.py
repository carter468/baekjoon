# Data Mining?
# Gold 3, simulation, implementation

import sys
input = sys.stdin.readline

def f(i,j):
    if grid[i][j] == 'M': return 99
    q = [(i,j)]
    visited = [[-1]*C for _ in range(R)] # -1:커버 0:오픈 1:깃발
    visited[i][j] = 0
    changed = True
    while changed:
        changed = False
        nq = []
        for x,y in q:
            f,m,c = 0,0,0
            for nx,ny in (x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1):
                if 0 <= nx < R and 0 <= ny < C:
                    if grid[nx][ny] == 'M':
                        m += 1
                    if visited[nx][ny] == 1:
                        f += 1
                    if visited[nx][ny] == -1:
                        c += 1
            if f == m:
                for nx,ny in (x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1):
                    if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == -1:
                        visited[nx][ny] = 0
                        nq.append((nx,ny))
                        changed = True
            elif f+c == m:
                for nx,ny in (x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1):
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 'M':
                        visited[nx][ny] = 1
                        changed = True
            else: nq.append((x,y))
        q = nq
    
    c = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.' and visited[i][j] == -1: c += 1
    return c

while True:
    R,C = map(int,input().split())
    if R == 0: break
    grid = [input() for _ in range(R)]

    m = 99
    for i in range(R):
        for j in range(C):
            m = min(m,f(i,j))
    print(m)