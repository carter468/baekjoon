# 벽 부수고 이동하기

from collections import deque

N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input())))

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    q = deque()
    q.append((0,0,0)) # x,y,벽 부수기 가능:0 벽 부수기 불가능:1

    while q:
        x,y,cheat = q.popleft()

        if x == N-1 and y == M-1:     # 도착
            return visited[x][y][cheat]
            
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M:     # 배열안에 있는 좌표
                if visited[nx][ny][cheat] == 0 and arr[nx][ny] == 0: #방문기록없고 이동가능
                    visited[nx][ny][cheat] = visited[x][y][cheat] + 1
                    q.append((nx,ny,cheat))                            
                elif arr[nx][ny] == 1 and cheat == 0:     #이동불가능하고 벽부수기 가능
                    visited[nx][ny][1] = visited[x][y][cheat] + 1
                    q.append((nx,ny,1))
    return -1

print(bfs())