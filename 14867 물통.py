# 물통
# Gold 2, BFS

from collections import deque

def check(x,y):
    if (x,y) not in visited:
        visited.add((x,y))
        q.append((x,y,count+1))

a,b,c,d = map(int,input().split())

visited = set([(0,0)])
q = deque([(0,0,0)])
while q:
    x,y,count = q.popleft()
    if (x,y) == (c,d):
        print(count)
        break
    check(a,y)
    check(x,b)
    check(0,y)
    check(x,0)
    z = x+y
    if z > a: check(a,z-a)
    else: check(z,0)
    if z > b: check(z-b,b)
    else: check(0,z)
else: print(-1)