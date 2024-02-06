# 화산쇄설류
# Gold 4, BFS

from collections import deque

m,n,v = map(int,input().split())
x,y = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]

vol = [[10**9]*n for _ in range(m)]
for _ in range(v):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    arr[a][b] = -1
    vol[a][b] = min(vol[a][b],c)
    q = deque([(a,b,c)])
    while q:
        a,b,c = q.popleft()
        for nx,ny in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
            if 0 <= nx < m and 0 <= ny < n and c+1 < vol[nx][ny]:
                vol[nx][ny] = c+1
                q.append((nx,ny,c+1))

x,y = x-1,y-1
visited = [[-1]*n for _ in range(m)]
visited[x][y] = 0
q = deque([(x,y)])
result = [-1,0]
while q:
    a,b = q.popleft()
    if arr[a][b] > result[0]: result = [arr[a][b],visited[a][b]]
    elif arr[a][b] == result: result[1] = min(result[1],visited[a][b])

    for nx,ny in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
        if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == -1 and visited[a][b]+1 < vol[nx][ny] and arr[nx][ny] != -1:
            visited[nx][ny] = visited[a][b]+1
            q.append((nx,ny))

print(*result)