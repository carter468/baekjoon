# 토마토

from collections import deque

m,n = map(int,input().split())      # 가로, 세로
tomato = []         # 익은토마토 1      익지않은토마토 0    빈상자 -1
q = deque()
for i in range(n):
    tomato.append(list(map(int,input().split())))
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i,j])

dx = [1,-1,0,0]
dy = [0,0,-1,1]
day = 0

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
                    # 상자 범위         익지않은토마토
            if 0<=nx<n and 0<=ny<m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append([nx,ny])
            
bfs()

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            quit()
    day = max(day,max(i)-1)

print(day)