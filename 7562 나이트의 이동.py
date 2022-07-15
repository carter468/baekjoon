# 나이트의 이동

dx = [-2,-2,2,2,1,-1,1,-1]                  # 이동방향
dy = [-1,1,-1,1,-2,-2,2,2]

def bfs():
    visited[start[0]][start[1]] = 1
    q = [[start[0],start[1]]]                # queue

    while q:
        x,y = q.pop(0)
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            # 체스 판 범위와 방문기록 확인
            if 0<=nx<I and 0<=ny<I and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx,ny])
            if nx == end[0] and ny == end[1]: # 도착
                print(visited[nx][ny]-1)        # 처음 시작점 제외해서 -1
                return 

T = int(input())
for _ in range(T):
    I = int(input())                                            # 체스판 크기
    start = list(map(int,input().split()))                      # 나이트의 위치
    end = list(map(int,input().split()))                        # 목표지점
    visited = [[0 for _ in range(I)] for _ in range(I)]         # 방문기록

    bfs()                                       