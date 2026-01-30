# 가상 키보드 입력
# Platinum 4, BFS

from collections import deque

R,C = map(int,input().split())
A = [input() for _ in range(R)]
S = input()+'*'
n = len(S)

move = [[[None]*4 for _ in range(C)] for _ in range(R)]
for x in range(R):
    for y in range(C):
        for dx,dy,k in (1,0,0),(-1,0,1),(0,1,2),(0,-1,3):
            nx,ny = x+dx,y+dy
            while 0 <= nx < R and 0 <= ny < C and A[nx][ny] == A[x][y]:
                nx += dx
                ny += dy
            if 0 <= nx < R and 0 <= ny < C:
                move[x][y][k] = (nx,ny)

visited = [[[-1]*(n+1) for _ in range(C)] for _ in range(R)]
visited[0][0][0] = 0
q = deque([(0,0,0)])
while q:
    x,y,z = q.popleft()
    nz = z
    if A[x][y] == S[z]: nz += 1
    if nz == n:
        exit(print(visited[x][y][z]+n))

    if visited[x][y][nz] == -1:
        visited[x][y][nz] = visited[x][y][z]
        q.appendleft((x,y,nz))

    for k in range(4):
        if move[x][y][k]:
            nx,ny = move[x][y][k]
            if visited[nx][ny][nz] == -1:
                visited[nx][ny][nz] = visited[x][y][z]+1
                q.append((nx,ny,nz))