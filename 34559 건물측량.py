# 건물 측량
# Gold 3, DFS, prefix sum

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
grid = [input() for _ in range(N)]

building = [[True]*M for _ in range(N)]
building[0][0] = False
q = [(0,0)]
while q:
    x,y = q.pop()
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == '0' and building[nx][ny]:
            building[nx][ny] = False
            q.append((nx,ny))

psum = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        psum[i][j] = psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]+building[i][j]

for _ in range(int(input())):
    r1,c1,r2,c2 = map(int,input().split())
    r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
    x = psum[r2][c2]-psum[r2][c1-1]-psum[r1-1][c2]+psum[r1-1][c1-1]
    if x == 0: print('Yes')
    else: print('No',x)