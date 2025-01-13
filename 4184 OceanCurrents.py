# Ocean Currents
# Gold 3, 0-1 BFS

from collections import deque

D = (-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)

R,C = map(int,input().split())
grid = [tuple(map(int,input())) for _ in range(R)]
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    a,b,c,d = a-1,b-1,c-1,d-1
    q = deque([(a,b)])
    visited = [[10**9]*C for _ in range(R)]
    visited[a][b] = 0
    while q:
        x,y = q.popleft()
        e = visited[x][y]
        if (x,y) == (c,d):
            print(e)
            break
        for i in range(8):
            nx,ny = x+D[i][0],y+D[i][1]
            if 0 <= nx < R and 0 <= ny < C:
                if i == grid[x][y]:
                    if visited[nx][ny] > e:
                        visited[nx][ny] = e
                        q.appendleft((nx,ny))
                else:
                    if visited[nx][ny] > e+1:
                        visited[nx][ny] = e+1
                        q.append((nx,ny))