# 미로에 갇힌 건우
# Gold 1, BFS

from collections import deque

n,m = map(int,input().split())
arr = [input().split() for _ in range(n)]

q = deque([(0,0,0)])
visited = [[[[-1]*2 for _ in range(m)] for _ in range(n)] for _ in range(n)]
visited[0][0][0][0] = 0
while q:
    x,y,z = q.popleft()
    night = z//m%2
    if (x,y) == (n-1,n-1):
        print(z//(m*2)+1,['sun','moon'][night])
        break

    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        nx,ny = x+dx,y+dy
        nz = z+1
        nnight = nz//m%2

        if nx < 0 or nx == n or ny < 0 or ny == n or visited[nx][ny][nz%m][nnight] != -1: continue
        
        if arr[nx][ny] == '0':
            visited[nx][ny][nz%m][nnight] = visited[x][y][z%m][night]+1
            q.append((nx,ny,nz))
        elif night:
            while 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == '0':
                    if visited[nx][ny][nz%m][nnight] == -1:
                        visited[nx][ny][nz%m][nnight] = visited[x][y][z%m][night]+1
                        q.append((nx,ny,nz))
                    break
                nx += dx
                ny += dy
else: print(-1)
