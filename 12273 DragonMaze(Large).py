# Dragon Maze (Large)
# Gold 3, BFS, DP

from collections import deque
import sys
input = sys.stdin.readline

for t in range(int(input())):
    N,M = map(int,input().split())
    sx,sy,ex,ey = map(int,input().split())
    arr = [tuple(map(int,input().split())) for _ in range(N)]
    
    visited = [[-1]*M for _ in range(N)]
    visited[sx][sy] = 0
    val = [[0]*M for _ in range(N)]
    val[sx][sy] = arr[sx][sy]
    q = deque([(sx,sy)])
    while q:
        x,y = q.popleft()
        if (x,y) == (ex,ey): break
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != -1:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y]+1
                    val[nx][ny] = val[x][y]+arr[nx][ny]
                    q.append((nx,ny))
                elif visited[nx][ny] == visited[x][y]+1:
                    val[nx][ny] = max(val[nx][ny],val[x][y]+arr[nx][ny])
    else:
        val[ex][ey] = 'Mission Impossible.'
    print(f'Case #{t+1}: {val[ex][ey]}')