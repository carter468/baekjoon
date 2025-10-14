# Checkpoint
# Gold 5, BFS

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y,end):
    visited = [[-1]*C for _ in range(R)]
    visited[x][y] = 0
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        if grid[x][y] == end:
            return x,y,visited[x][y]
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#' and visited[nx][ny] == -1:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y]+1

for _ in range(int(input())):
    R,C,D = map(int,input().split())
    grid = [input() for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'S':
                x,y = i,j

    result = 0
    for i in range(D):
        x,y,d = bfs(x,y,str(i+1))
        result += d
    result += bfs(x,y,'E')[2]
    print(result)