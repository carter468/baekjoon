# 통나무 옮기기
# Gold 2, BFS, 구현

from collections import deque
import sys
input = sys.stdin.readline

def check1(x,y):
    if x < 0 or x == n or y < 0 or y == n or m[x][y] == '1': 
        return False
    return True

def check2(x,y):
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)):
        nx,ny = x+dx,y+dy
        if nx < 0 or nx == n or ny < 0 or ny == n or m[nx][ny] == '1':
            return False
    return True

n = int(input())
m = [list(input()) for _ in range(n)]
ds,de = 0,0
for i in range(n):
    for j in range(n):
        if m[i][j] == 'B':
            m[i][j] = '0'
            if ds == 0:
                if i+1 < n and m[i+1][j] == 'B':
                    s = (i+1,j)
                    ds = (1,0)
                else:
                    s = (i,j+1)
                    ds = (0,1)
        elif m[i][j] == 'E':
            m[i][j] = '0' 
            if de == 0:
                if i+1 < n and m[i+1][j] == 'E':
                    e = (i+1,j)
                    de = (1,0)
                else:
                    e = (i,j+1)
                    de = (0,1)

visit = [[[-1]*2 for _ in range(n)] for _ in range(n)]
visit[s[0]][s[1]][ds[0]] = 0
q = deque([(s,ds)])
while q:
    lo,di = q.popleft()
    if lo == e and di == de:
        print(visit[lo[0]][lo[1]][di[0]])
        break

    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx,ny = lo[0]+dx, lo[1]+dy
        if check1(nx,ny) and check1(nx+di[0],ny+di[1]) and check1(nx-di[0],ny-di[1]) and visit[nx][ny][di[0]] == -1:
            visit[nx][ny][di[0]] = visit[lo[0]][lo[1]][di[0]] + 1
            q.append(((nx,ny),di))

    if check2(lo[0],lo[1]) and visit[lo[0]][lo[1]][di[1]] == -1:
        visit[lo[0]][lo[1]][di[1]] = visit[lo[0]][lo[1]][di[0]] + 1
        q.append((lo,(di[1],di[0])))
else:
    print(0)