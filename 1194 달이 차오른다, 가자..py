# 달이 차오른다, 가자
# Gold 1, BFS, bitmask

from collections import deque

n,m = map(int,input().split())
arr = [input() for _ in range(n)]

def s():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '0': return i,j

visited = [[[-1]*64 for _ in range(m)] for _ in range(n)]
i,j = s()
visited[i][j][0] = 0
q = deque([(i,j,0)])
while q:
    x,y,z = q.popleft()
    if arr[x][y] == '1':
        print(visited[x][y][z])
        break
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][z] == -1:
            a = arr[nx][ny]
            if a == '#': continue
            if a in 'ABCDEF' and z>>(ord(a)-65)&1 == 0: continue
            if a in 'abcdef': 
                nz = z|1<<(ord(a)-97)
                visited[nx][ny][nz] = visited[x][y][z]+1
                q.append((nx,ny,nz))
            else:
                visited[nx][ny][z] = visited[x][y][z]+1
                q.append((nx,ny,z))
else: print(-1)