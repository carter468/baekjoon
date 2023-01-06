# 그림
# Silver 1, 너비 우선 탐색

from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j):
    q = deque([(i,j)])
    visit[i][j] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                visit[nx][ny] = True
                if array[nx][ny]=='1':
                    cnt += 1
                    q.append((nx,ny))
    return cnt

dx = [1,0,0,-1]
dy = [0,1,-1,0]
n,m = map(int,input().split())
array = []
for _ in range(n):
    array.append(tuple(input().split()))
visit = [[False for _ in range(m)] for _ in range(n)]

painting = []
for i in range(n):
    for j in range(m):
        if not visit[i][j] and array[i][j] == '1':
            painting.append(bfs(i,j))

print(len(painting))
print(max(painting) if painting else 0)