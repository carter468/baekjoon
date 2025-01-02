# 위치 바꾸기
# Gold 3, BFS

from collections import deque
D = (1,0),(1,-1),(1,1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1),(0,0)

N,M = map(int,input().split())
board = [input() for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'A':
            Ax,Ay = i,j
        elif board[i][j] == 'B':
            Bx,By = i,j

visited = [[[[-1]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[Ax][Ay][Bx][By] = 0
q = deque([(Ax,Ay,Bx,By)])
while q:
    x1,y1,x2,y2 = q.popleft()
    if (x1,y1,x2,y2) == (Bx,By,Ax,Ay):
        print(visited[x1][y1][x2][y2])
        break

    for dx1,dy1 in D:
        x3,y3 = x1+dx1,y1+dy1
        if 0 <= x3 < N and 0 <= y3 < M and board[x3][y3] != 'X':
            for dx2,dy2 in D:
                x4,y4 = x2+dx2,y2+dy2
                if 0 <= x4 < N and 0 <= y4 < M and board[x4][y4] != 'X' and (x3,y3) != (x4,y4) and (x1,y1,x2,y2) != (x4,y4,x3,y3) and visited[x3][y3][x4][y4] == -1:
                    visited[x3][y3][x4][y4] = visited[x1][y1][x2][y2]+1
                    q.append((x3,y3,x4,y4))
else: print(-1)