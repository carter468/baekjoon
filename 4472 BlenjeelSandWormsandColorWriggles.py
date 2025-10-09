# Blenjeel Sand Worms and Color Wriggles
# Platinum 5, BFS

from collections import deque

while True:
    grid = []
    while True:
        g = input()
        if g == 'end': exit()
        if g == '': break
        grid.append(g)

    N,M = len(grid),len(grid[0])

    c = set()
    arr = []
    e = []
    for i in range(N):
        c.add(grid[i][0])
        arr.append((i,0))
        e.append((i,M-1))
    
    visited = {tuple(arr)}
    q = deque([(c,arr,0)])
    while q:
        c,arr,d = q.popleft()
        if arr == e or arr == e[::-1]:
            print(d)
            break

        for _ in range(2):
            for dx,dy in (1,0),(-1,0),(0,-1),(0,1):
                x,y = arr[-1]
                tx,ty = arr[0]
                
                nx,ny = x+dx,y+dy
                if 0 <= nx < N and 0 <= ny < M:
                    nc = set(c)
                    nc.remove(grid[tx][ty])
                    narr = arr[1:]+[(nx,ny)]
                    if tuple(narr) not in visited and tuple(narr[::-1]) not in visited and grid[nx][ny] not in nc:
                        visited.add(tuple(narr))
                        nc.add(grid[nx][ny])
                        q.append((nc,narr,d+1))
            arr = arr[::-1]

    else: print(-1)