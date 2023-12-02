# 폴리큐브의 겉넓이
# Gold 3, implementation

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    point = []
    n = int(input())
    for _ in range((n-1)//8+1):
        for p in input().split():
            point.append(tuple(map(int,p.split(','))))

    if point[0] != (0,0,0):
        print('NO 1')
        continue

    cube = [[[0]*5 for _ in range(5)] for _ in range(5)]
    cube[0][0][0] = 1
    area = 6
    result = ''
    for i in range(1,n):
        x,y,z = point[i]
        a = 6
        for nx,ny,nz in (x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1):
            if 0 <= nx <= 4 and 0 <= ny <= 4 and 0 <= nz <= 4 and cube[nx][ny][nz] == 1:
                a -= 2
        if a == 6 or cube[x][y][z] == 1:
            result = 'NO '+str(i+1)
            break
        area += a
        cube[x][y][z] = 1

    print(result if result else area)