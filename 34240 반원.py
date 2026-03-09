# 반원
# Gold 2, geometry

import sys
input = sys.stdin.readline

def dist(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

def dot(p1,p2):
    return p1[0]*p2[0]+p1[1]*p2[1]

def cross(p1,p2):
    return p1[0]*p2[1]-p1[1]*p2[0]

points = [tuple(map(int,input().split())) for _ in range(int(input()))]
xa,ya,xb,yb = map(int,input().split())

A = xa,ya
B = xb,yb
C = xa*2-xb,ya*2-yb
AB = (xb-xa,yb-ya)
dAB = dot(AB,AB)
r = dist(A,B)

result = 0
for P in points:
    x,y = P
    AP = (x-xa,y-ya)
    cr = cross(AB,AP)
    if cr < 0:
        if -dAB <= dot(AP,AB) <= dAB:
            result += abs(cr/r)
        else:
            result += min(dist(B,P),dist(C,P))
    else:
        result += max(0,dist(A,P)-r)
print(result)