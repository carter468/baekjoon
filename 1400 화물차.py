# 화물차
# Gold 1, dijkstra, implementation

import heapq

while True:
    m,n = map(int,input().split())
    if m == 0: break

    grid = [input() for _ in range(m)]
    dist = [[10**9]*n for _ in range(m)]
    arr = []
    while True:
        try:
            _,a,b,c = input().split()
            arr.append((a,int(b),int(c)))
        except:
            break

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'A':
                dist[i][j] = 0
                q = [(0,i,j)]
            elif grid[i][j] == 'B':
                ex,ey = i,j
    
    while q:
        d,x,y = heapq.heappop(q)
        if d > dist[x][y]: continue
        d += 1
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx,ny = x+dx,y+dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '.':
                if grid[nx][ny] in '#AB':
                    if d < dist[nx][ny]:
                        dist[nx][ny] = d
                        heapq.heappush(q,(d,nx,ny))
                else:
                    a,b,c = arr[int(grid[nx][ny])]
                    r,s = divmod(d-1,b+c)
                    if a == '-':
                        if dy != 0:
                            if s < b: t = d
                            else: t = d+b+c-s
                        else:
                            if s < b: t = d+b-s
                            else: t = d
                    else:
                        if dx != 0:
                            if s < c: t = d
                            else: t = d+b+c-s
                        else:
                            if s < c: t = d+c-s
                            else: t = d
                    if t < dist[nx][ny]:
                        dist[nx][ny] = t
                        heapq.heappush(q,(t,nx,ny))
    
    print(dist[ex][ey] if dist[ex][ey] != 10**9 else 'impossible')