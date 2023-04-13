# 수영장 만들기
# Gold 1, BFS

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global result

    q = deque([(j,k)])
    flag = 1
    visit[j][k] = 1
    cnt = 1
    while q:
        x,y = q.popleft()
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx,y+dy
            if nx < 0 or nx == n or ny < 0 or ny == m:
                flag = 0
                continue
            if grid[nx][ny] <= i and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1
    if flag:
        result += cnt

n,m = map(int,input().split())
grid = [tuple(map(int,input().strip())) for _ in range(n)]

result = 0
for i in range(1,9):
    visit = [[0]*m for _ in range(n)]
    for j in range(n):
        for k in range(m):
            if grid[j][k] <= i and not visit[j][k]:
                bfs()

print(result)