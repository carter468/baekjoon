# 마법사 상어와 토네이도
# Gold 3, implementation, simulation

def tornado():
    def sand():
        global result
        if 0 <= nx < N and 0 <= ny < N: arr[nx][ny] += m
        else: result += m

    c = arr[x][y]
    arr[x][y] = 0
    t = 0

    if dx == 0:
        nxnyp = (x+1,y+dy,10),(x-1,y+dy,10),(x+1,y,7),(x-1,y,7),(x+2,y,2),(x-2,y,2),(x+1,y-dy,1),(x-1,y-dy,1)
    else:
        nxnyp = (x+dx,y+1,10),(x+dx,y-1,10),(x,y+1,7),(x,y-1,7),(x,y+2,2),(x,y-2,2),(x-dx,y+1,1),(x-dx,y-1,1)
    for nx,ny,p in nxnyp:
        m = c*p//100
        t += m
        sand()

    nx,ny,m = x+dx*2,y+dy*2,c*5//100
    t += m
    sand()
    nx,ny,m = x+dx,y+dy,c-t
    sand()

D = (0,-1),(1,0),(0,1),(-1,0)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

result = 0
x,y = N//2,N//2
for i in range(N*2-1):
    dx,dy = D[i%4]
    for _ in range(min(i//2+1,N-1)):
        x += dx
        y += dy
        tornado()

print(result)