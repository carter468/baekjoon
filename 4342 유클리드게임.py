# 유클리드 게임
# Gold 2, game theory

while True:
    a,b = map(int,input().split())
    if a == 0: break
    t = 0
    if a < b: a,b = b,a
    while a%b != 0 and a//b < 2:
        a,b = b,a%b
        t ^= 1
    print('AB'[t]+' wins')