# 쌓기 나무
# Gold 4, 구현

import sys
input = sys.stdin.readline

def check():
    for i in range(n):
        if max(grid[i]) != right[-1-i]:
            return False
    for i in range(m):
        a = 0
        for j in range(n):
            a = max(a,grid[j][i])
        if a != front[i]:
            return False
    return True
    
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
front = tuple(map(int,input().split()))
right = tuple(map(int,input().split()))

for i in range(n):
    for j in range(m):
        if grid[i][j]:
            grid[i][j] = min(front[j],right[-1-i])
            
if check():
    for i in grid:
        print(*i)
else:
    print(-1)