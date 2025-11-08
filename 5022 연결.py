# 연결
# Gold 1, BFS

from collections import deque

def solve(p1,p2,p3,p4):
    x1,y1,x2,y2,x3,y3,x4,y4 = *p1,*p2,*p3,*p4

    q = deque([(x1,y1,0)])
    visited = [[None]*M for _ in range(N)]
    visited[x1][y1] = visited[x3][y3] = visited[x4][y4] = True
    while q:
        x,y,d = q.popleft()
        if (x,y) == (x2,y2): break
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = (x,y)
                q.append((nx,ny,d+1))
    
    grid = [[True]*M for _ in range(N)]
    while (x,y) != (x1,y1):
        grid[x][y] = False
        x,y = visited[x][y]
    grid[x][y] = False

    q = deque([(x3,y3)])
    visited = [[-1]*M for _ in range(N)]
    visited[x3][y3] = 0
    while q:
        x,y = q.popleft()
        if (x,y) == (x4,y4): return d+visited[x][y]
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
    return 10**9

N,M = map(int,input().split())
A1,A2 = tuple(map(int,input().split())),tuple(map(int,input().split()))
B1,B2 = tuple(map(int,input().split())),tuple(map(int,input().split()))

N,M = N+1,M+1
result = min(solve(A1,A2,B1,B2),solve(B1,B2,A1,A2))
print(result if result < 10**9 else 'IMPOSSIBLE')