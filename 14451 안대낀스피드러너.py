# 안대 낀 스피드러너
# Platinum 5, BFS

from collections import deque
dx = -1,0,1,0
dy = 0,1,0,-1

def move(x,y,d):
    if (x,y) != (0,n-1):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 'E':
            return nx,ny
    return x,y

n = int(input())
grid = [input() for _ in range(n)]

visited = [[[[[[-1]*4 for _ in range(n)] for _ in range(n)] for _ in range(4)] for _ in range(n)] for _ in range(n)]
visited[-1][0][0][-1][0][1] = 0
q = deque([(n-1,0,0,n-1,0,1)])
while q:
    x1,y1,d1,x2,y2,d2 = q.popleft()
    k = visited[x1][y1][d1][x2][y2][d2]
    if (x1,y1,x2,y2) == (0,n-1,0,n-1):
        print(k)
        break

    for dd in (1,-1):
        nd1,nd2 = (d1+dd)%4,(d2+dd)%4
        if visited[x1][y1][nd1][x2][y2][nd2] == -1:
            visited[x1][y1][nd1][x2][y2][nd2] = k+1
            q.append((x1,y1,nd1,x2,y2,nd2))
    
    x1,y1 = move(x1,y1,d1)
    x2,y2 = move(x2,y2,d2)
    if visited[x1][y1][d1][x2][y2][d2] == -1:
        visited[x1][y1][d1][x2][y2][d2 ] = k+1
        q.append((x1,y1,d1,x2,y2,d2))
