# 테트리스 게임
# Gold 5, 브루트포스

import sys
input = sys.stdin.readline

arr_23 = [ [[1,0],[0,2]], [[1,0],[1,1]], [[0,1],[0,2]], [[0,0],[0,2]], [[1,0],[1,2]] ]
arr_32 = [ [[0,0],[2,1]], [[1,1],[2,1]], [[0,0],[1,0]], [[0,0],[2,0]], [[0,1],[2,1]] ]
t = 1

while (n:=int(input())):
    grid = [tuple(map(int,input().split())) for _ in range(n)]
    result = -sys.maxsize
    # 가로막대
    for i in range(n):
        for j in range(n-3):
            result = max(result,sum(grid[i][j:j+4]))
    # 세로막대
    for i in range(n-3):
        for j in range(n):
            result = max(result,grid[i][j]+grid[i+1][j]+grid[i+2][j]+grid[i+3][j])
    # 정사각형
    for i in range(n-1):
        for j in range(n-1):
            result = max(result,grid[i][j]+grid[i+1][j]+grid[i][j+1]+grid[i+1][j+1])
    # 2X3 직사각형에서 두개빼기
    for i in range(n-1):
        for j in range(n-2):
            temp = sum(grid[i][j:j+3])+sum(grid[i+1][j:j+3])
            for k in arr_23:
                result = max(result,temp-grid[i+k[0][0]][j+k[0][1]]-grid[i+k[1][0]][j+k[1][1]])
    # 3X2 직사각형에서 두개빼기
    for i in range(n-2):
        for j in range(n-1):
            temp = sum(grid[i][j:j+2])+sum(grid[i+1][j:j+2])+sum(grid[i+2][j:j+2])
            for k in arr_32:
                result = max(result,temp-grid[i+k[0][0]][j+k[0][1]]-grid[i+k[1][0]][j+k[1][1]])

    print(f'{t}. {result}')
    t += 1