# 편세권
# Gold 5, BFS

from collections import deque
import sys
input = sys.stdin.readline

n,m,r,c = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(r)]

q = deque()
visited = [[-1]*(m+1) for _ in range(n+1)]
for _ in range(c):
    a,b = map(int,input().split())
    q.append((a,b))
    visited[a][b] = 0

while q:
    x,y = q.popleft()
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 1 <= nx <= n and 1 <= ny <= m and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y]+1
            q.append((nx,ny))

result = 10**9
for a,b,p in arr:
    result = min(result,visited[a][b]*p)
print(result)
