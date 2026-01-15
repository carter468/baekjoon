# 볼록 격자 다각형의 내부점
# Gold 1, bruteforcing, geometry

import sys,math
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(N)]
    y1,y2 = 30,-30
    for x,y in arr:
        y1 = min(y1,y)
        y2 = max(y2,y)

    result = []
    for y in range(y2,y1,-1):
        xs = []
        for i in range(N):
            x1,y1 = arr[i-1]
            x2,y2 = arr[i]
            if y1 <= y < y2 or y2 <= y < y1:
                x = x1+(y-y1)*(x2-x1)/(y2-y1)
                xs.append(x)
        
        if xs:
            xs.sort()
            l = math.ceil(xs[0]+1e-9)
            r = math.floor(xs[-1]-1e-9)
            if l <= r:
                result.append((y,l,r))

    print(len(result))
    for r in result: print(*r)