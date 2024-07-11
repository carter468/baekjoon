# 소년 점프
# Gold 4, BFS

from collections import deque
M = 10**5

r,c = map(int,input().split())
arr = [input() for _ in range(r)]
visited = [[[M]*3 for _ in range(c)] for _ in range(r)]
for i in range(3):
    x,y = map(int,input().split())
    x,y = x-1,y-1
    visited[x][y][i] = 0
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '0' and visited[nx][ny][i] == M:
                visited[nx][ny][i] = visited[x][y][i]+1
                q.append((nx,ny))

result = [M,0]
for i in range(r):
    for j in range(c):
        m = max(visited[i][j])
        if m != M and m < result[0]:
            result = [m,1]
        elif m == result[0]:
            result[1] += 1

if result[0] == M:
    print(-1)
else:
    print(result[0])
    print(result[1])