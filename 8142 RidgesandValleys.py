# Ridges and Valleys
# Gold 3, DFS

import sys
input = sys.stdin.readline

def dfs(i,j,m):
    f1 = f2 = True
    visited[i][j] = True
    q = [(i,j)]
    while q:
        x,y = q.pop()
        for dx,dy in (0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1):
            nx,ny = x+dx,y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] > m:
                    f1 = False
                elif grid[nx][ny] < m:
                    f2 = False
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
    if f1: count[0] += 1
    if f2: count[1] += 1

N = int(input())
grid = [tuple(map(int,input().split())) for _ in range(N)]

count = [0,0]
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j,grid[i][j])
print(*count)