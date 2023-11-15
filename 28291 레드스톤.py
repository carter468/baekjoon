# 레드스톤
# Gold 5, BFS, implementation

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    q = deque([(x,y)])
    visit = [[-1]*H for _ in range(W)]
    visit[x][y] = 0
    while q:
        x,y = q.popleft()
        if visit[x][y] == 15: break
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < W and 0 <= ny < H and grid[nx][ny] > 0 and visit[nx][ny] == -1:
                if grid[nx][ny] == 1: return True
                if grid[nx][ny] == 2:
                    q.append((nx,ny))
                    visit[nx][ny] = visit[x][y]+1
    return False

W,H = map(int,input().split())
grid = [[0]*H for _ in range(W)]
lamp = []
for _ in range(int(input())):
    B,X,Y = input().split()
    X,Y = int(X),int(Y)
    if B == 'redstone_block': grid[X][Y] = 1 
    elif B == 'redstone_dust': grid[X][Y] = 2 
    else: lamp.append((X,Y)) 

for x,y in lamp:
    if bfs(x,y) == False: 
        print('failed')
        break
else:
    print('success')