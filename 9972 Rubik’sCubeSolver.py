# Rubik’s Cube Solver
# Platinum 5, implementation, simulation

import sys
input = sys.stdin.readline

pos = {'left':0,'front':1,'right':2,'back':3,'top':4,'bottom':5}
dir = {'left':0,'right':1}

def rotate1(i,dir):
    temp = [f[:] for f in face[i]]
    if dir == 0:
        for x,y,nx,ny in (0,0,2,0),(0,1,1,0),(0,2,0,0),(1,0,2,1),(1,2,0,1),(2,0,2,2),(2,1,1,2),(2,2,0,2):
            face[i][nx][ny] = temp[x][y]
    else:
        for x,y,nx,ny in (0,0,0,2),(0,1,1,2),(0,2,2,2),(1,0,0,1),(1,2,2,1),(2,0,0,0),(2,1,1,0),(2,2,2,0):
            face[i][nx][ny] = temp[x][y]

def rotate2(arr,dir):
    temp = []
    for i in range(6):
        temp.append([f[:] for f in face[i]])

    for i in range(12):
        x,y,z = arr[i]
        if dir == 0:
            nx,ny,nz = arr[i-3]
        else:
            nx,ny,nz = arr[i-9]
        face[nx][ny][nz] = temp[x][y][z]

while input()[0] == 'S':
    arr = [input().split() for _ in range(9)]

    face = []
    for i in range(4):
        temp = []
        for j in range(3,6):
            temp.append(arr[j][i*3:i*3+3])
        face.append(temp)
    temp = []
    for i in range(3):
        temp.append(arr[i])
    face.append(temp)
    temp = []
    for i in range(6,9):
        temp.append(arr[i])
    face.append(temp)

    while True:
        op = input().split()
        if len(op) == 1: break

        a,b = pos[op[0]],dir[op[1]]
        rotate1(a,b)

        if a == 0:
            arr = (4,0,0),(4,1,0),(4,2,0),(1,0,0),(1,1,0),(1,2,0),(5,0,0),(5,1,0),(5,2,0),(3,2,2),(3,1,2),(3,0,2)
        elif a == 1:
            arr = (4,2,0),(4,2,1),(4,2,2),(2,0,0),(2,1,0),(2,2,0),(5,0,2),(5,0,1),(5,0,0),(0,2,2),(0,1,2),(0,0,2)
        elif a == 2:
            arr = (4,2,2),(4,1,2),(4,0,2),(3,0,0),(3,1,0),(3,2,0),(5,2,2),(5,1,2),(5,0,2),(1,2,2),(1,1,2),(1,0,2)
        elif a == 3:
            arr = (0,0,0),(0,1,0),(0,2,0),(5,2,0),(5,2,1),(5,2,2),(2,2,2),(2,1,2),(2,0,2),(4,0,2),(4,0,1),(4,0,0)
        elif a == 4:
            arr = (1,0,2),(1,0,1),(1,0,0),(0,0,2),(0,0,1),(0,0,0),(3,0,2),(3,0,1),(3,0,0),(2,0,2),(2,0,1),(2,0,0)
        elif a == 5:
            arr = (1,2,0),(1,2,1),(1,2,2),(2,2,0),(2,2,1),(2,2,2),(3,2,0),(3,2,1),(3,2,2),(0,2,0),(0,2,1),(0,2,2)
        rotate2(arr,b)
        
    for i in range(6):
        if len(set().union(*face[i])) != 1:
            print('No')
            break
    else:
        print('Yes')