# 열쇠
# Gold 1, BFS

from collections import deque,defaultdict
import sys
input = sys.stdin.readline

def checkEntry():
    if grid[i][j] == '*': return 
    if 'A' <= grid[i][j] <= 'Z':
        door[grid[i][j]].append((i,j))
        return 
    q.append((i,j))
    visit[i][j] = 1
    if grid[i][j] == '$':
        grid[i][j] = '.'
        return 1
    elif 'a' <= grid[i][j] <= 'z':
        keys.add(grid[i][j])
        grid[i][j] = '.'

def openDoor():
    for c in door:
        if c.lower() not in keys: continue
        while door[c]:
            x,y = door[c].pop()
            grid[x][y] = '.'
            q.append((x,y))
            visit[x][y] = 1

for _ in range(int(input())):
    h,w = map(int,input().split())
    grid = [list(input()) for _ in range(h)]

    result = 0
    keys = set(input())
    door = defaultdict(list)
    q = deque()
    visit = [[0]*w for _ in range(h)]

    for i in (0,h-1):
        for j in range(w):
            if checkEntry(): result += 1
    for i in range(1,h-1):
        for j in (0,w-1):
            if checkEntry(): result += 1
    openDoor()

    while q:
        x,y = q.popleft()
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx,y+dy
            if nx < 0 or nx == h or ny < 0 or ny == w or visit[nx][ny] or grid[nx][ny] == '*': continue
            if 'A' <= grid[nx][ny] <= 'Z':
                door[grid[nx][ny]].append((nx,ny))
                continue
            if grid[nx][ny] == '$': 
                result += 1
            elif 'a' <= grid[nx][ny] <= 'z':
                keys.add(grid[nx][ny])
            q.append((nx,ny))
            visit[nx][ny] = 1
            grid[nx][ny] = '.'
        if not q:
            openDoor()

    print(result)