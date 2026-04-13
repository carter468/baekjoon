# 인내의 도미노 장인 호석
# Gold 5, implementation, simulation

import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())
grid = [tuple(map(int,input().split())) for _ in range(N)]

result = [['S']*M for _ in range(N)]
count = 0
for _ in range(R):
    x,y,d = input().split()
    dx,dy = {'E':(0,1),'W':(0,-1),'N':(-1,0),'S':(1,0)}[d]
    
    x,y = int(x)-1,int(y)-1
    if result[x][y] == 'F': continue
    result[x][y] = 'F'
    q = [(x,y)]
    while q:
        x,y = q.pop()
        count += 1
        for _ in range(grid[x][y]-1):
            x += dx
            y += dy
            if x < 0 or x == N or y < 0 or y == M: break
            if result[x][y] == 'S':
                result[x][y] = 'F'
                q.append((x,y))
    
    x,y = map(int,input().split())
    result[x-1][y-1] = 'S'

print(count)
for r in result:
    print(*r)