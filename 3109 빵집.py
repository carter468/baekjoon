# 빵집
# Gold 2, DFS, greedy

import sys
input = sys.stdin.readline

def dfs(x,y):
    if y == C-1: return True
    
    ny = y+1
    for nx in (x-1,x,x+1):
        if 0 <= nx < R and grid[nx][ny] == '.' and not visited[nx][ny]:
            visited[nx][ny] = True
            if dfs(nx,ny): return True
    return False
    
R,C = map(int,input().split())
grid = [input() for _ in range(R)]

visited = [[False]*C for _ in range(R)]
count = 0
for i in range(R):
    if dfs(i,0): count += 1
print(count)