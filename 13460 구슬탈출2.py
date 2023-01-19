# 구슬 탈출 2
# Gold 1, 구현, 너비 우선 탐색

import sys
input = sys.stdin.readline
dx = (1,-1,0,0)
dy = (0,0,1,-1)

def solve(r,b):
    nq = [(r,b)]
    visit = [(r,b)]
    for count in range(1,11):
        q = nq
        nq = []
        while q:
            r,b = q.pop()
            for i in range(4):
                rx,ry = r
                bx,by = b
                flag = [False,False]    # 정지상태
                hole = [False,False]    # 구멍에 들어갔다
                while not all(flag):
                    if not flag[0]:
                        rx += dx[i]
                        ry += dy[i]
                    if not flag[1]:
                        bx += dx[i]
                        by += dy[i]

                    # 벽에 막힘
                    if board[rx][ry] == '#':
                        rx -= dx[i]
                        ry -= dy[i]
                        flag[0] = True
                    if board[bx][by] == '#':
                        bx -= dx[i]
                        by -= dy[i]
                        flag[1] = True

                    # 구멍에 들어감
                    if board[rx][ry] == 'O':
                        hole[0] = True
                        flag[0] = True
                    if board[bx][by] == 'O':
                        hole[1] = True
                        flag[1] = True

                    if all(hole):   # 두공다 구멍에
                        break

                    if (rx,ry)==(bx,by):
                        if flag[0]: # 빨간공 정지상태
                            bx -= dx[i]
                            by -= dy[i]
                            flag[1] = True
                        else:       # 파란공 정지상태
                            rx -= dx[i]
                            ry -= dy[i]
                            flag[0] = True

                if hole == [True,False]:   # 빨간공이 빠졌다
                    return count
                elif r==(rx,ry) and b==(bx,by): # 움직이지 않았다
                    continue
                elif hole == [False,False]:
                    if ((rx,ry),(bx,by)) not in visit:
                        nq.append(((rx,ry),(bx,by)))
                        visit.append(((rx,ry),(bx,by)))

    return -1

N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == 'B':
            b = (i,j)
        if board[i][j] == 'R':
            r = (i,j)

print(solve(r,b))