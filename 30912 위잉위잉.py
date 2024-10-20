# 위잉위잉
# Gold 4, implementation, geometry

from functools import cmp_to_key
import sys
input = sys.stdin.readline

def cmp(p1,p2):
    if len(p1) == 3:
        x1,y1,d1 = 0,0,p1[0]
        x2,y2,d2 = 0,0,p2[0]
    elif len(p1) == 5:
        x1,y1,d1 = p1[:3]
        x2,y2,d2 = p2[:3]
    if x2*y1 > x1*y2: return 1
    elif x2*y1 < x1*y2: return -1
    elif d1 > d2: return 1
    else: return -1

arr = [tuple(map(int,input().split())) for _ in range(int(input()))]
xh,yh = map(int,input().split())

quadrant1,quadrant2,quadrant3,quadrant4 = [],[],[],[] # 각 사분면
xp,xm,yp,ym = [],[],[],[] # 축을 양쪽방향으로 4개로 나눔

for x,y in arr:
    d = (x-xh)**2+(y-yh)**2
    if x == xh: # y축
        if y > yh: yp.append((d,x,y))
        else: ym.append((d,x,y))
    elif y == yh: # x축
        if x > xh: xp.append((d,x,y))
        else: xm.append((d,x,y))
    elif x > xh and y > yh: # 제1사분면
        quadrant1.append((x-xh,y-yh,d,x,y))
    elif x < xh and y > yh: # 제2사분면
        quadrant2.append((xh-x,yh-y,d,x,y))
    elif x < xh and y < yh: # 제3사분면
        quadrant3.append((xh-x,yh-y,d,x,y))
    elif x > xh and y < yh: # 제4사분면
        quadrant4.append((x-xh,y-yh,d,x,y))

for p in (xp,quadrant1,yp,quadrant2,xm,quadrant3,ym,quadrant4):
    for a in sorted(p,key=cmp_to_key(cmp)):
        print(*a[-2:])