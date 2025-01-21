# 다오의 데이트
# Gold 4, backtracking

def solve(x,y,c,result):
    if grid[x][y] == 'Z':
        exit(print('YES',result,sep='\n'))
    if c == N: return

    for d in marid[c]:
        dx,dy = MOVE[d]
        nx,ny = x+dx,y+dy
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '@':
            solve(nx,ny,c+1,result+d)

MOVE = {'W':(-1,0),'A':(0,-1),'S':(1,0),'D':(0,1)}

H,W = map(int,input().split())
grid = [input() for _ in range(H)]
N = int(input())
marid = [input().split() for _ in range(N)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == 'D':
            x,y = i,j

solve(x,y,0,'')
print('NO')