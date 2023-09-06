# Good Pizza, Great Pizza
# Gold 4, geometry

import sys
INF = sys.maxsize

r1,r2,r3,r4 = INF,-INF,INF,-INF
for _ in range(int(input())):
    x,y = map(int,sys.stdin.readline().split())
    k1,k2 = y-x,y+x
    r1,r2 = min(r1,k1),max(r2,k1)
    r3,r4 = min(r3,k2),max(r4,k2)
a = max(r2-r1,r4-r3)
if a%2 == 0: print(a*a//2)
else: print(str(a*a//2)+'.5')