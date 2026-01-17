# Windblume Festival
# Gold 4, ad hoc

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    if int(input()) == 1:
        print(int(input()))
        continue
    x = 10**9
    y = -x
    f = True
    s = 0
    for a in map(int,input().split()):
        if a > 0:
            x = min(x,a)
            f = False
        else:
            x = 0
            y = max(y,a)
        s += abs(a)
    if f == True: s += y*2
    else: s -= x*2
    print(s)