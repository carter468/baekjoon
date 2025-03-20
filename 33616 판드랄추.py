# 판드랄추
# Gold 1, ad hoc, bitmask

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,b = map(int,input().split())
    if (a+b)%2 == 1: print(-1)
    else:
        a1,a2,b1,b2 = 0,0,0,0
        for i in range(30):
            if a>>i&1 != b>>i&1:
                x = 1<<(i-1)
                c = 2-(a>>(i-1)&1)
                if a < b:
                    for _ in range(c):
                        a += x
                        b ^= x
                    b1 += x
                    if c == 2: b2 += x
                else:
                    for _ in range(c):
                        b += x
                        a ^= x
                    a1 += x
                    if c == 2: a2 += x

        k = 0
        for x in (a1,a2,b1,b2):
            if x: k += 1
        print(k)
        if a1: print('A',a1)
        if a2: print('A',a2)
        if b1: print('B',b1)
        if b2: print('B',b2)