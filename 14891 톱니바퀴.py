# 톱니바퀴
# Gold 5, implementation, simulation

gear = [input() for _ in range(4)]
rotate = [0]*4
for _ in range(int(input())):
    a,b = map(int,input().split())
    temp = [0]*4
    if a == 1:
        temp[0] = -b
        if gear[0][(2+rotate[0])%8] != gear[1][(-2+rotate[1])%8]:
            temp[1] = b
            if gear[1][(2+rotate[1])%8] != gear[2][(-2+rotate[2])%8]:
                temp[2] = -b
                if gear[2][(2+rotate[2])%8] != gear[3][(-2+rotate[3])%8]:
                    temp[3] = b
    elif a == 2:
        temp[1] = -b
        if gear[1][(2+rotate[1])%8] != gear[2][(-2+rotate[2])%8]:
            temp[2] = b
            if gear[2][(2+rotate[2])%8] != gear[3][(-2+rotate[3])%8]:
                temp[3] = -b
        if gear[0][(2+rotate[0])%8] != gear[1][(-2+rotate[1])%8]:
            temp[0] = b
    elif a == 3:
        temp[2] = -b
        if gear[2][(2+rotate[2])%8] != gear[3][(-2+rotate[3])%8]:
            temp[3] = b
        if gear[1][(2+rotate[1])%8] != gear[2][(-2+rotate[2])%8]:
            temp[1] = b
            if gear[0][(2+rotate[0])%8] != gear[1][(-2+rotate[1])%8]:
                temp[0] = -b
    else:
        temp[3] = -b
        if gear[2][(2+rotate[2])%8] != gear[3][(-2+rotate[3])%8]:
            temp[2] = b
            if gear[1][(2+rotate[1])%8] != gear[2][(-2+rotate[2])%8]:
                temp[1] = -b
                if gear[0][(2+rotate[0])%8] != gear[1][(-2+rotate[1])%8]:
                    temp[0] = b
    for i in range(4):
        rotate[i] += temp[i]
    
result = 0
for i in range(4):
    result += int(gear[i][rotate[i]%8])*2**i
print(result)