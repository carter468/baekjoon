# Aquarium
# Gold 2, DFS, MST

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

for t in range(int(input())):
    R,C = map(int,input().split())
    arr = [input() for _ in range(R)]
    s = [tuple(map(int,input().split())) for _ in range(R)]
    grid = [[0]*(C*2) for _ in range(R*2)]    
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '/':
                grid[i*2][j*2+1] = grid[i*2+1][j*2] = s[i][j]
            else:
                grid[i*2][j*2] = grid[i*2+1][j*2+1] = s[i][j]

    num = [[0]*(C*2) for _ in range(R*2)]
    c = 0
    for i in range(R*2):
        for j in range(C*2):
            if grid[i][j] == 0 and num[i][j] == 0:
                c += 1
                num[i][j] = c
                q = [(i,j)]
                while q:
                    x,y = q.pop()
                    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < R*2 and 0 <= ny < C*2 and grid[nx][ny] == 0 and num[nx][ny] == 0 and (x//2,y//2) != (nx//2,ny//2):
                            num[nx][ny] = c
                            q.append((nx,ny))
                    for dx,dy in (1,1),(-1,1),(1,-1),(-1,-1):
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < R*2 and 0 <= ny < C*2 and grid[nx][ny] == 0 and num[nx][ny] == 0 and (x//2,y//2) != (nx//2,ny//2) and abs(x//2-nx//2)+abs(y//2-ny//2) < 2:
                            num[nx][ny] = c
                            q.append((nx,ny))

    edge = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '/': edge.append((grid[i*2][j*2+1],num[i*2][j*2],num[i*2+1][j*2+1]))
            else: edge.append((grid[i*2][j*2],num[i*2+1][j*2],num[i*2][j*2+1]))
    edge.sort()

    root = list(range(c+1))
    result = 0
    for d,x,y in edge:
        x,y = find(x),find(y)
        if x != y:
            root[x] = y
            result += d

    print(f'Case {t+1}: {result}')