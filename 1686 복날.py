# 복날
# Gold 4, BFS

from collections import deque

def dist(a,b,c,d):
    return (a-c)**2+(b-d)**2

v,m = map(float,input().split())
sx,sy = map(float,input().split())
ex,ey = map(float,input().split())
b = set()
while 1:
    try:
        a = input()
        if not a: break 
        b.add(tuple(map(float,a.split())))
    except: break

d = (v*m*60)**2
q = deque([(sx,sy,0)])
visit = set()
while q:
    x,y,c = q.popleft()
    if dist(x,y,ex,ey) < d:
        print(f'Yes, visiting {c} other holes.')
        break
    for nx,ny in b:
        if (nx,ny) not in visit and dist(x,y,nx,ny) < d:
            visit.add((nx,ny))
            q.append((nx,ny,c+1))
else: print('No.')