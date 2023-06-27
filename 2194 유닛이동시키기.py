# 유닛 이동시키기
# Gold 5, BFS

from collections import deque
import sys
input = sys.stdin.readline
dx = (1,-1,0,0)
dy = (0,0,1,-1)

def check():
    if nx == 0 or nx > n or ny == 0 or ny > m or nx+a-1 > n or ny+b-1 > m or grid[nx][ny] == 1 or visit[nx][ny] != -1: return False
    
    if i == 0:    # down
        for j in range(b):
            if grid[nx+a-1][ny+j]==1:
                return False
            
    if i == 1:    # up
        for j in range(b):
            if grid[nx][ny+j]==1:
                return False
            
    if i == 2:    # right
        for j in range(a):
            if grid[nx+j][ny+b-1]==1:
                return False
            
    if i == 3:    # left
        for j in range(a):
            if grid[nx+j][ny]==1:
                return False
            
    return True

n,m,a,b,k = map(int,input().split())
grid = [[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    c,d = map(int,input().split())
    grid[c][d] = 1
s = tuple(map(int,input().split()))
e = tuple(map(int,input().split()))

q = deque([s])
visit = [[-1]*(m+1) for _ in range(n+1)]
visit[s[0]][s[1]] = 0
while q:
    x,y = q.popleft()
    if (x,y) == e:
        print(visit[x][y])
        break
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if check():
            visit[nx][ny] = visit[x][y]+1
            q.append((nx,ny))
else:
    print(-1)