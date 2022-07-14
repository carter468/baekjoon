# 미로탐색

import sys
input = sys.stdin.readline

# n,m = 4,6       # 세로 가로
# maze = ['101111','101010','101011','111011']    # 시작[0][0] , 도착[n-1][m-1]

n,m = map(int,input().split())
maze = []
for _ in range(n):
    maze.append(str(input().strip()))

# 상하좌우 탐색
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[0 for _ in range(m)] for _ in range(n)] # 방문기록

def bfs():      # 0,0 시작
    global cnt
    visited[0][0] = 1   

    q = [[0,0]]
    while q:
        z = q.pop(0)
        i = z[0]
        j = z[1]

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<=n-1 and 0<=ny<=m-1 and maze[nx][ny] == '1' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[i][j] + 1
                q.append([nx,ny])
                if nx==n-1 and ny==m-1:     # 도착
                    return visited[nx][ny]

print(bfs())