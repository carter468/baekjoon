# Colored Bead Works
# Platinum 4, DP, probability, bitmask, case work, implementation

def f(arr):
    x = 0
    for i in range(4):
        for j in range(4):
            x += 3**(i*4+j)*C.get(arr[i][j],0)
    return x

def g(x):
    arr = [['']*4 for _ in range(4)]
    for i in range(16):
        x,y = divmod(x,3)
        arr[i//4][i%4] = 'EGW'[y]
    return arr

def h(arr):
    ii = 0,1,2,3
    jj = 0,1,2,3
    if a == 'R':
        jj = 3,2,1,0
    elif a == 'B':
        ii = 3,2,1,0
    for i in ii:
        for j in jj:
            if arr[i][j] != 'E':
                x,y = i,j
                while True:
                    nx,ny = x+dx,y+dy
                    if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny] == 'E':
                        arr[nx][ny],arr[x][y] = arr[x][y],arr[nx][ny]
                    else:
                        break
                    x,y = nx,ny
    return arr

C = {'G':1,'W':2}
D = {'L':(0,-1),'R':(0,1),'T':(-1,0),'B':(1,0)}
M = (1,1),(1,2),(2,1),(2,2)
E = (0,1,2,3,4,7,8,11,12,13,14,15)

for _ in range(int(input())):
    _,*actions = input().split()
    result = [input() for _ in range(4)]

    dic = {0:1}
    for a in actions:
        ndic = dict()

        if a in 'GW':
            for x in dic:
                arr = g(x)
                e = 0
                for i,j in M:
                    if arr[i][j] == 'E':
                        e += 1
                if e in (1,2,4):
                    for i,j in M:
                        if arr[i][j] == 'E':
                            nx = x+3**(i*4+j)*C[a]
                            ndic[nx] = ndic.get(nx,0)+dic[x]/e
                elif e == 3:
                    for i,j in M:
                        if arr[i][j] != 'E':
                            i,j = 3-i,3-j
                            nx = x+3**(i*4+j)*C[a]
                            ndic[nx] = ndic.get(nx,0)+dic[x]
                elif e == 0:
                    for k in E:
                        i,j = divmod(k,4)
                        if arr[i][j] == 'E': e += 1
                    for k in E:
                        i,j = divmod(k,4)
                        if arr[i][j] == 'E':
                            nx = x+3**k*C[a]
                            ndic[nx] = ndic.get(nx,0)+dic[x]/e
        else:
            dx,dy = D[a]
            ndic = dict()
            for x in dic:
                nx = f(h(g(x)))
                ndic[nx] = ndic.get(nx,0)+dic[x]
        dic = ndic

    print(dic.get(f(result),0))