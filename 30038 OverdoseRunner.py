# Overdose Runner
# Gold 1, implementation

def lvup():
    while info[4] >= info[3]:
        info[4] -= info[3]
        info[3] += 10
        info[0] += info[5]
        info[1] += 1
        info[5] += 1

def atk(a,b):
    if grid[a][b] == '*': return 0
    if grid[a][b] == 'm':
        i = idx[(a,b)]
        h[i] -= max(0,info[0]-d[i])
        if h[i] <= 0:
            grid[a][b] = '.'
            info[4] += e[i]
    return 1

n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]
input()
h = list(map(int,input().split()))
d = tuple(map(int,input().split()))
e = tuple(map(int,input().split()))
input()

info = [5,1,1,10,0,1,0,0,0]
c = 0
idx = {}
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'p':
            grid[i][j] = '.'
            x,y = i,j
        if grid[i][j] == 'm':
            idx[(i,j)] = c
            c += 1
for c in input().split():
    if c == 'u':
        nx = x-info[2]
        if 0 < nx < n and grid[nx][y] in '.g':
            x = nx
            info[6] += 1
            info[8] -= 1
    elif c == 'd':
        nx = x+info[2]
        if 0 < nx < n and grid[nx][y] in '.g':
            x = nx
            info[6] += 1
            info[8] -= 1
    elif c == 'l':
        ny = y-info[2]
        if 0 < ny < m and grid[x][ny] in '.g':
            y = ny
            info[6] += 1
            info[8] -= 1
    elif c == 'r':
        ny = y+info[2]
        if 0 < ny < m and grid[x][ny] in '.g':
            y = ny
            info[6] += 1
            info[8] -= 1
    elif c == 'w':
        info[6] += 1
        info[8] -= 1
    elif info[8] > 0: continue
    elif c == 'au':
        info[6] += 3
        for dx in range(1,info[1]+1):
            if atk(x-dx,y) == 0: break
        lvup()
    elif c == 'ad':
        info[6] += 3
        for dx in range(1,info[1]+1):
            if atk(x+dx,y) == 0: break
        lvup()
    elif c == 'al':
        info[6] += 3
        for dy in range(1,info[1]+1):
            if atk(x,y-dy) == 0: break
        lvup()
    elif c == 'ar':
        info[6] += 3
        for dy in range(1,info[1]+1):
            if atk(x,y+dy) == 0: break
        lvup()
    elif c == 'du':
        info[6] += 2
        info[2] += 1
        info[7] += 1
        if info[7]%5 == 0:
            info[8] = 10
    elif c == 'dd':
        info[6] += 2
        info[2] = max(0,info[2]-1)
        info[7] += 1
        if info[7]%5 == 0:
            info[8] = 10
    elif c == 'c':
        if grid[x][y] == 'g':
            break

grid[x][y] = 'p'
print(info[5],info[4])
print(info[6])
for i in grid:
    print(''.join(i))
for i in h:
    if i > 0:
        print(i,end=' ')