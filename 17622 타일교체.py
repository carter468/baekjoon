# 타일 교체
# Gold 2, BFS, implementation

from collections import deque

A = {(0,2):3,(0,3):1,(0,4):0,(1,0):0,(1,2):2,(1,5):1,(2,0):3,(2,1):1,(2,4):2,(3,1):0,(3,3):2,(3,5):3}
B = {0:(1,0),1:(0,-1),2:(-1,0),3:(0,1)}

N,K = map(int,input().split())
grid = [tuple(map(int,input().split())) for _ in range(N)]

q = deque([(0,0,3,0)])
visited = [[[[0]*2 for _ in range(4)] for _ in range(N)] for _ in range(N)]
visited[0][0][3][0] = 1
while q:
    x,y,z,k = q.popleft()

    nz = A.get((z,grid[x][y]),-1)
    if nz != -1:
        dx,dy = B[nz]
        nx,ny = x+dx,y+dy
        if (nx,ny) == (N-1,N) and (k == K or visited[x][y][z][k] != N*N):
            exit(print(visited[x][y][z][k]))
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny][nz][k] == 0:
            visited[nx][ny][nz][k] = visited[x][y][z][k]+1
            q.append((nx,ny,nz,k))
    
    if k < K:
        for d in range(6):
            nz = A.get((z,d),-1)
            if d == grid[x][y] or nz == -1: continue
            dx,dy = B[nz]
            nx,ny = x+dx,y+dy
            if (nx,ny) == (N-1,N):
                exit(print(visited[x][y][z][k]))
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny][nz][1] == 0:
                visited[nx][ny][nz][1] = visited[x][y][z][0]+1
                q.append((nx,ny,nz,1))

print(-1)