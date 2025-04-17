# 로하의 농사
# Gold 5, backtracking

def solve(x,y,c,t,d):
    global result
    
    if c > p: return
    result = max(result,t)

    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        nx,ny = x+dx,y+dy
        if nx < 0 or nx == N or ny < 0 or ny == M or visited[nx][ny]: continue
        visited[nx][ny] = True
        nt = t+W[nx][ny]
        if dx != 0:
            if d == 1: nc = c+1
            else: nc = c+2
        else:
            if d == 1: nc = c+2
            else: nc = c+1
        solve(nx,ny,nc,nt,dx*dx)
        visited[nx][ny] = False

N,M = map(int,input().split())
W = [tuple(map(int,input().split())) for _ in range(N)]
x,y,p = map(int,input().split())

result = 0
visited = [[False]*M for _ in range(N)]
visited[x][y] = True
for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
    nx,ny = x+dx,y+dy
    if nx < 0 or nx == N or ny < 0 or ny == M or visited[nx][ny]: continue
    visited[nx][ny] = True
    solve(nx,ny,1,W[nx][ny],dx*dx)
    visited[nx][ny] = False

print(result+W[x][y])