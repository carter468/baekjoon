# 정산소
# Gold 4, math

import sys
input = sys.stdin.readline

n,q = map(int,input().split())

t = n*(n+1)//2
r,c = set(),set()
sr,sc = 0,0
for _ in range(q):
    a,b = input().split()
    b = int(b)
    if a == 'R':
        if b in r: print(0)
        else:
            print(t+(n-len(c))*b-sc)
            r.add(b)
            sr += b
    else:
        if b in c: print(0)
        else:
            print(t+(n-len(r))*b-sr)
            c.add(b)
            sc += b