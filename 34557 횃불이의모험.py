# 횃불이의 모험
# Gold 5, implementation

D = (-1,0),(0,-1),(1,0),(0,1)

N,M = map(int,input().split())
grid = [input().split() for _ in range(N)]
keyevent = [input() for _ in range(4)]

for i in range(N):
    for j in range(N):
        if grid[i][j] == '2':
            x,y = i,j

prev = -1
for cur in input():
    cur = 'WASD'.index(cur)
    for i in range(4):
        event = None
        if prev != i and cur == i: event = 'Down'
        if prev == i and cur == i: event = 'Stay'
        if prev == i and cur != i: event = 'Up'
        if event == keyevent[i]:
            dx,dy = D[i]
            nx,ny = x+dx,y+dy
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != '1':
                x,y = nx,ny
    prev = cur
print(x+1,y+1)