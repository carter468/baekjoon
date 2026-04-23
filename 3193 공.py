# 공
# Gold 4, implementation

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
grid = [list(input()) for _ in range(N)]

arr = [[[None]*N for _ in range(N)] for _ in range(4)]
# 아래
for i in range(N-1,-1,-1):
    for j in range(N):
        if grid[i][j] != 'X':
            if i+1 < N and arr[0][i+1][j]:
                arr[0][i][j] = arr[0][i+1][j]
            else:
                arr[0][i][j] = (i,j)
# 오른쪽 
for i in range(N):
    for j in range(N-1,-1,-1):
        if grid[i][j] != 'X':
            if j+1 < N and arr[1][i][j+1]:
                arr[1][i][j] = arr[1][i][j+1]
            else:
                arr[1][i][j] = (i,j)
# 위
for i in range(N):
    for j in range(N):
        if grid[i][j] != 'X':
            if i-1 >= 0 and arr[2][i-1][j]:
                arr[2][i][j] = arr[2][i-1][j]
            else:
                arr[2][i][j] = (i,j)
# 왼쪽
for i in range(N):
    for j in range(N):
        if grid[i][j] != 'X':
            if j-1 >= 0 and arr[3][i][j-1]:
                arr[3][i][j] = arr[3][i][j-1]
            else:
                arr[3][i][j] = (i,j)
        if grid[i][j] == 'L':
            grid[i][j] = '.'
            x,y = i,j

d = 0
for _ in range(K):
    if input()[0] == 'D': d = (d+1)%4
    else: d = (d-1)%4
    x,y = arr[d][x][y]
grid[x][y] = 'L'

for _ in range(d):
    result = [['']*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][-1-i] = grid[i][j]
    grid = result

for g in grid:
    print(''.join(g).strip())