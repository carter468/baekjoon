# 현수막
# Silver 1, 깊이 우선 탐색

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
dx = 1,1,1,0,0,-1,-1,-1
dy = 1,0,-1,1,-1,1,0,-1

def dfs(x,y):
    for i in range(8):
        nx,ny = x+dx[i],y+dy[i]
        if nx<0 or nx==M or ny<0 or ny==N or board[nx][ny] == '0':
            continue
        board[nx][ny] = '0'
        dfs(nx,ny)

M,N = map(int,input().split())
board = [list(input().split()) for _ in range(M)]

count = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == '1':
            count += 1
            dfs(i,j)
print(count)