# 추진기
# Gold 2, constructive, ad hoc

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    L,R = map(int,input().split())

    if (R+1)//2 < L or L == R:
        if L == R:
            result = [L]
        else:
            result = [L,-R]
        t = 1
        for i in range(R-1,L,-1):
            result.append(i*t)
            t *= -1
        print(*result)
    else:
        x = (R+1)//2
        result = [x,-R]
        t = 1
        for i in range(R-1,L-1,-1):
            if i == x: continue
            result.append(i*t)
            t *= -1
        print(*result)