# Cross Spider
# Platinum 5, geometry

import sys
input = sys.stdin.readline

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

N = int(input())
P = [tuple(map(int,input().split())) for _ in range(N)]

if N <= 3: exit(print('TAK'))

p1,p2 = P[:2]
for i in range(2,N):
    p3 = P[i]
    v1 = (p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2])
    v2 = (p3[0]-p1[0],p3[1]-p1[1],p3[2]-p1[2])
    nvec = cross(v1,v2)
    if nvec != (0,0,0): break
else: exit(print('TAK'))

result = 'TAK'
for p in P:
    vp = (p[0]-p1[0],p[1]-p1[1],p[2]-p1[2])
    if dot(vp,nvec) != 0:
        result = 'NIE'
        break

print(result)