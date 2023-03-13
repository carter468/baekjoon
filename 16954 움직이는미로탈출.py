# 움직이는 미로 탈출
# Gold 3, bfs

from collections import deque

def escape():
    grid = [tuple(input()) for _ in range(8)]

    w = [[[] for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if grid[i][j]=='#':
                for k in range(i,8):
                    w[k][j].append(k-i)

    q = deque([(7,0,0)])
    while q:
        x,y,t = q.popleft()
        for dx,dy in ((0,-1),(0,0),(0,1),(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1)):
            nx,ny = x+dx,y+dy
            if nx==0 and ny==7: return 1
            if nx<0 or nx>7 or ny<0 or ny>7 or t+1 in w[nx][ny] or t in w[nx][ny]: continue
            q.append((nx,ny,t+1))
    return 0

print(escape())