# 알파벳
# Gold 4, backtracking

import sys
input = sys.stdin.readline

def bt(x,y,count):
    global result
    result = max(result,count)
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0<=nx<r and 0<=ny<c and abc[ord(grid[nx][ny])-65]==False:
            abc[ord(grid[nx][ny])-65] = True
            bt(nx,ny,count+1)
            abc[ord(grid[nx][ny])-65] = False

r,c = map(int,input().split())
grid = [input() for _ in range(r)]

abc = [False]*26
abc[ord(grid[0][0])-65] = True

result = 0
bt(0,0,1)
print(result)