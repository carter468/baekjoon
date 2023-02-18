# 주사위 굴리기
# Gold 4, 구현, 시뮬레이션

import sys
input = sys.stdin.readline

N,M,x,y,_ = map(int,input().split())
table = [input().split() for _ in range(N)]

dice = ['0']*6    # [동서남북상하]
for i in input().split():
    if i=='1':
        if y+1==M: continue
        dice = [dice[4],dice[5],dice[2],dice[3],dice[1],dice[0]]
        y += 1
    elif i=='2':
        if y-1==-1: continue
        dice = [dice[5],dice[4],dice[2],dice[3],dice[0],dice[1]]
        y -= 1
    elif i=='3':
        if x-1==-1: continue
        dice = [dice[0],dice[1],dice[5],dice[4],dice[2],dice[3]]
        x -= 1
    else:
        if x+1==N: continue
        dice = [dice[0],dice[1],dice[4],dice[5],dice[3],dice[2]]
        x += 1
    if table[x][y]!='0':
        dice[5],table[x][y] = table[x][y],'0'
    else:
        table[x][y] = dice[5]
        
    print(dice[4])