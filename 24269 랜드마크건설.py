# 랜드마크 건설
# Gold 1, case work

import sys
input = sys.stdin.readline
M = 8*10**8

for _ in range(int(input())):
    a,b,c = map(int,input().split())

    m = max(a,b,c)
    if (a+b+c)%2 != 0 or m*2 > a+b+c:
        print(-1)
        continue

    if m == a:
        if b < c:
            x1,y1 = 1,1
            y2 = min(a+1,M)
            x2 = a+2-y2
            x3 = (b+c+x2-y2+2)//2
            y3 = c+2-x3
        else:
            x2,y2 = 1,1
            y1 = min(a+1,M)
            x1 = a+2-y1
            x3 = (b+c+x1-y1+2)//2
            y3 = b+2-x3
    elif m == b:
        if a > c:
            x2,y2 = 1,1
            y3 = min(b+1,M)
            x3 = b+2-y3
            x1 = (a+c+x3-y3+2)//2
            y1 = a+2-x1
        else:
            x3,y3 = 1,1
            y2 = min(b+1,M)
            x2 = b+2-y2
            x1 = (a+c+x2-y2+2)//2
            y1 = c+2-x1
    elif m == c:
        if a < b:
            x3,y3 = 1,1
            y1 = min(c+1,M)
            x1 = c+2-y1
            x2 = (a+b+x1-y1+2)//2
            y2 = b+2-x2
        else:
            x1,y1 = 1,1
            y3 = min(c+1,M)
            x3 = c+2-y3
            x2 = (a+b+x3-y3+2)//2
            y2 = a+2-x2

    print(x1,y1,x2,y2,x3,y3)