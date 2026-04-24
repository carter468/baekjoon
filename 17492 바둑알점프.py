# 바둑알 점프
# Gold 4, bruteforcing, backtracking

def solve():
    c = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == '2':
                c += 1
                for dx,dy in (1,0),(-1,0),(1,1),(0,1),(-1,1),(1,-1),(0,-1),(-1,-1):
                    x1,y1 = x+dx,y+dy
                    x2,y2 = x1+dx,y1+dy
                    if 0 <= x2 < N and 0 <= y2 < N and arr[x1][y1] == '2' and arr[x2][y2] == '0':
                        arr[x][y],arr[x1][y1],arr[x2][y2] = '0','0','2'
                        solve()
                        arr[x][y],arr[x1][y1],arr[x2][y2] = '2','2','0'
    if c == 1: exit(print('Possible'))

N = int(input())
arr = [input().split() for _ in range(N)]

solve()
print('Impossible')