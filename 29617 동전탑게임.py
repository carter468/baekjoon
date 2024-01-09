# 동전 탑 게임
# Platinum 4, game theory

a,b,k = map(int,input().split())

if k < 0:
    if a+b == 1: print('Second')
    elif (a,b) == (1,1): print('First')
    elif k == -1: print('First')
    elif a == b: print('Second')
    else: print('First')
else:
    if a == b: print('Second')
    else: print('First')