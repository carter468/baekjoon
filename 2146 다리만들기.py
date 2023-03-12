# 다리 만들기
# Gold 3, bfs

from collections import deque
import sys
input = sys.stdin.readline

def numbering(num):
    q = deque([(i,j)])
    grid[i][j] = num
    while q:
        x,y = q.popleft()
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]=='1':
                grid[nx][ny] = num
                q.append((nx,ny))

def find_length(num):
    visit = [[-1]*n for _ in range(n)]
    q = deque([(i,j)])
    visit[i][j] = 0
    while q:
        x,y = q.popleft()
        if visit[x][y]>=answer:
            break
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx,y+dy
            if nx<0 or nx==n or ny<0 or ny==n or grid[nx][ny]==num or visit[nx][ny]!=-1: continue
            if grid[nx][ny]=='0':
                visit[nx][ny] = visit[x][y]+1
                q.append((nx,ny))
            else:
                return visit[x][y]
    return answer

n = int(input())
grid = [list(input().split()) for _ in range(n)]

num = 1
for i in range(n):
    for j in range(n):
        if grid[i][j]=='1':
            numbering(num)
            num += 1

answer = sys.maxsize
for i in range(n):
    for j in range(n):
        if grid[i][j]!='0':
            answer = find_length(grid[i][j])

print(answer)