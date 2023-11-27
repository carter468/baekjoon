# 마방진
# Gold 3, implementation

square = [list(map(int,input().split())) for _ in range(3)]

if square[0][0]+square[1][1]+square[2][2] == 0 or square[2][0]+square[1][1]+square[0][2] == 0:
    target = 0
    for i in square:
        target += sum(i)
    target //= 2
else:
    for i in square:
        if 0 not in i:
            target = sum(i)
            break
    else:
        for i in range(3):
            if square[0][i]*square[1][i]*square[2][i] != 0:
                target = square[0][i]+square[1][i]+square[2][i]
                break
        else:
            if square[0][0]*square[1][1]*square[2][2] != 0:
                target = square[0][0]+square[1][1]+square[2][2]
            else:
                target = square[2][0]+square[1][1]+square[0][2]

for i in range(3):
    for j in range(3):
        if square[i][j] == 0:
            if square[i][j-1] and square[i][j-2]:
                square[i][j] = target-square[i][j-1]-square[i][j-2]
            elif square[i-1][j] and square[i-2][j]:
                square[i][j] = target-square[i-1][j]-square[i-2][j]
            elif (i,j) in [(0,0),(2,2)]:
                square[i][j] = target-square[i-1][j-1]-square[i-2][j-2]
            elif (i,j) in [(0,2),(2,0)]:
                square[i][j] = target-square[i-1][j-2]-square[i-2][j-1]
            elif (i,j) == (1,1):
                square[i][j] = target-square[0][0]-square[2][2]

for i in square:
    print(*i)