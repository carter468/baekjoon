# 4연산
# Gold 5, BFS

from collections import deque

s,t = map(int,input().split())

q = deque([(s,'')])
visit = set()
while q:
    x,y = q.popleft()
    if x == t:
        print(y if y else 0)
        break
    if x*x not in visit and x*x <= t:
        q.append((x*x,y+'*'))
        visit.add(x*x)
    if x+x not in visit and x+x <= t:
        q.append((x+x,y+'+'))
        visit.add(x+x)
    if 1 not in visit:
        q.append((1,y+'/'))
        visit.add(1)
else:
    print(-1)