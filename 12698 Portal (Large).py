# Portal (Large)
# Platinum 5, BFS

from collections import deque

for t in range(int(input())):
    R,C = map(int,input().split())
    grid = ['#'*(C+2)]
    for _ in range(R):
        grid.append('#'+input()+'#')
    grid.append(grid[0])

    q = deque()
    visited = [[None]*(C+1) for _ in range(R+1)]
    portal = [[[] for _ in range(C+1)] for _ in range(R+1)]
    for i in range(1,R+1):
        for j in range(1,C+1):
            if grid[i][j] == '#': continue
            if grid[i][j] == 'O':
                q.append((i,j,0,{(i,j)}))
                visited[i][j] = set()
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                x,y = i,j
                while grid[x+dx][y+dy] != '#':
                    x += dx
                    y += dy
                portal[i][j].append((x,y))

    answer = 'THE CAKE IS A LIE'
    while q:
        x,y,d,v = q.popleft()
        
        if grid[x][y] == 'X':
            answer = d
            break

        s = set()
        for i,j in v:
            for px,py in portal[i][j]:
                s.add((px,py))
        for px,py in portal[x][y]:
            s.add((px,py))

        f = False
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if grid[nx][ny] != '#':
                if visited[nx][ny] == None or (nx,ny) not in visited[nx][ny]:
                    if visited[nx][ny] == None: visited[nx][ny] = set()
                    else: visited[nx][ny].add((nx,ny))
                    nv = v.copy()
                    nv.add((nx,ny))
                    q.append((nx,ny,d+1,nv))
            else: f = True
        
        if f:
            for nx,ny in s:
                if visited[nx][ny] == None:
                    visited[nx][ny] = set()
                    q.append((nx,ny,d+1,set()))
        
    print(f'Case #{t+1}: {answer}')