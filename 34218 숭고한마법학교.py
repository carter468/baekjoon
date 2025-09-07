# 숭고한 마법학교
# Gold 4, BFS

from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [input().split() for _ in range(N)]
sr,sc = map(int,input().split())
er,ec = map(int,input().split())

arr = deque()
q = [(sr-1,sc-1)]
visited = [[False]*M for _ in range(N)]
visited[sr-1][sc-1] = True
while q:
    arr.append(q[-1])
    x,y = q.pop()
    A[x][y] = 's'
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and A[nx][ny] == '1':
            visited[nx][ny] = True
            q.append((nx,ny))
if A[er-1][ec-1] == 's': exit(print(0))

q = [(er-1,ec-1)]
while q:
    x,y = q.pop()
    A[x][y] = 'e'
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and A[nx][ny] == '1':
            visited[nx][ny] = True
            q.append((nx,ny))

visited = [[0]*M for _ in range(N)]
while arr:
    x,y = arr.popleft()
    if A[x][y] == 'e':
        print(visited[x][y])
        break

    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < M and A[nx][ny] != 's' and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y]+1
            arr.append((nx,ny))