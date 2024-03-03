# 모노미노도미노 2
# Gold 2, implementation, simulation

import sys
input = sys.stdin.readline

def getPos(col,k):
    for i in range(6):
        if block[k][i][col]: break
    else: return 5
    return i-1

def getScore(k):
    global score

    i = 5
    while i > 1:
        while sum(block[k][i]) == 4:
            score += 1
            for j in range(4):
                for h in range(i,0,-1):
                    block[k][h][j] = block[k][h-1][j]
        i -= 1

def delLine(k):
    a = (sum(block[k][0]) > 0)+(sum(block[k][1]) > 0)
    for j in range(4):
        for i in range(5,1,-1):
            block[k][i][j] = block[k][i-a][j]
        block[k][0][j],block[k][1][j] = 0,0
    
score = 0
block = [[[0]*4 for _ in range(6)] for _ in range(2)]

for _ in range(int(input())):
    t,x,y = map(int,input().split())
    if t == 1:
        block[0][getPos(y,0)][y] = 1
        block[1][getPos(x,1)][x] = 1
    elif t == 2:
        a = min(getPos(y,0),getPos(y+1,0))
        block[0][a][y],block[0][a][y+1] = 1,1
        a = getPos(x,1)
        block[1][a][x],block[1][a-1][x] = 1,1
    else:
        a = getPos(y,0)
        block[0][a][y],block[0][a-1][y] = 1,1
        a = min(getPos(x,1),getPos(x+1,1))
        block[1][a][x],block[1][a][x+1] = 1,1
    for i in (0,1): getScore(i),delLine(i)

count = 0
for i in range(6):
    count += sum(block[0][i])+sum(block[1][i])
print(score,count,sep='\n')