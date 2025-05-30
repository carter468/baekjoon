# 딸깍
# Gold 4, DFS, implementation

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [input() for _ in range(N)]

visited = [[False]*M for _ in range(N)]
visited[0][0] = True
c = 1
q = [(0,0)]
while q:
    x,y = q.pop()
    
    if arr[x][y] in '02356789':
        nx = x-1
        if nx >= 0 and arr[nx][y] in '0235689' and not visited[nx][y]:
            visited[nx][y] = True
            q.append((nx,y))
            c += 1
    if arr[x][y] in '0235689':
        nx = x+1
        if nx < N and arr[nx][y] in '02356789' and not visited[nx][y]:
            visited[nx][y] = True
            q.append((nx,y))
            c += 1
    if arr[x][y] in '01234789':
        ny = y+1
        if ny < M and arr[x][ny] in '045689' and not visited[x][ny]:
            visited[x][ny] = True
            q.append((x,ny))
            c += 1
    if arr[x][y] in '013456789':
        ny = y+1
        if ny < M and arr[x][ny] in '0268' and not visited[x][ny]:
            visited[x][ny] = True
            q.append((x,ny))
            c += 1
    if arr[x][y] in '045689':
        ny = y-1
        if ny >= 0 and arr[x][ny] in '01234789' and not visited[x][ny]:
            visited[x][ny] = True
            q.append((x,ny))
            c += 1
    if arr[x][y] in '0268':
        ny = y-1
        if ny >= 0 and arr[x][ny] in '013456789' and not visited[x][ny]:
            visited[x][ny] = True
            q.append((x,ny))
            c += 1

print('YES' if c == N*M else 'NO')