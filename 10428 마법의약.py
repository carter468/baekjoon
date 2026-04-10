# 마법의 약
# Platinum 4, math

for _ in range(int(input())):
    N,E = map(int,input().split())
    x = 0
    while (E+1)**x < N:
        x += 1
    print(x)