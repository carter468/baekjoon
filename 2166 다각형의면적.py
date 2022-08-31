# 다각형의 면적

import sys

def ccw(x1,y1,x2,y2,x3,y3):
    return x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)

n = int(input())
xy = []
for _ in range(n):
    xy.append(list(map(int,sys.stdin.readline().split())))

ans = 0
for i in range(n-2):
    ans += ccw(xy[0][0],xy[0][1],xy[i+1][0],xy[i+1][1],xy[i+2][0],xy[i+2][1])
print(f'{abs(ans/2):.1f}')