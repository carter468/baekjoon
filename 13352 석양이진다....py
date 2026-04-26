# 석양이 진다...
# Platinum 4, geometry, randomization

import sys,random
input = sys.stdin.readline

if (N:=int(input())) < 5: exit(print('success'))
P = [tuple(map(int,input().split())) for _ in range(N)]

for _ in range(99):
    a,b = random.sample(P,2)
    x1,y1,x2,y2 = *a,*b
    
    p = []
    for x,y in P:
        if (x1-x)*(y1-y2) != (x1-x2)*(y1-y):
            p.append((x,y))

    if len(p) < 3:
        exit(print('success'))
    x1,y1,x2,y2 = *p[0],*p[1]
    for x,y in p:
        if (x1-x)*(y1-y2) != (x1-x2)*(y1-y):
            break
    else:
        exit(print('success'))
print('failure')