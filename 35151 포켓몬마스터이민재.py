# 포켓몬 마스터 이민재
# Gold 4, greedy, case work

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r,HP = map(int,input().split())
    f = int(input())

    a = r/765
    if a >= 1:
        print('C')
    elif a*1.5 >= 1:
        print('GC')
    else:
        d = 0
        hp = HP
        while hp > 1:
            hp = max(1,hp-f)
            d += 1
            x = (1-2*hp/3/HP)*r/255
            if x >= 1:
                print('F'*d+'C')
                break
            if x*2.5 >= 1:
                print('Y'+'F'*d+'C')
                break
        else:
            print('Y'+'F'*max(1,d)+'C')