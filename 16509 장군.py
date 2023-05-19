# 장군
# Gold 5, BFS

from collections import deque

r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())

visit = [[-1]*9 for _ in range(10)]
visit[r1][c1] = 0
q = deque([(r1,c1)])
while q:
    x,y = q.popleft()
    if (x,y) == (r2,c2):
        break
    for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx,ny = x+dx,y+dy
        if nx < 0 or nx > 9 or ny < 0 or ny > 8 or (nx,ny) == (r2,c2): continue
        if dx == 0:
            for dx in (1,-1):
                nnx,nny = nx+dx*2,ny+dy*2
                if nnx < 0 or nnx > 9 or nny < 0 or nny > 8 or (nx+dx,ny+dy) == (r2,c2) or visit[nnx][nny] != -1: continue
                visit[nnx][nny] = visit[x][y]+1
                q.append((nnx,nny))
        else:
            for dy in (1,-1):
                nnx,nny = nx+dx*2,ny+dy*2
                if nnx < 0 or nnx > 9 or nny < 0 or nny > 8 or (nx+dx,ny+dy) == (r2,c2) or visit[nnx][nny] != -1: continue
                visit[nnx][nny] = visit[x][y]+1
                q.append((nnx,nny))
                
print(visit[r2][c2])