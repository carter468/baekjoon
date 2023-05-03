# 암벽 등반
# Gold 4, BFS

from collections import deque
import sys
input = sys.stdin.readline

n,t = map(int,input().split())
s = set([tuple(map(int,input().split())) for _ in range(n)])

q = deque([(0,0)])
visit = {}
visit[(0,0)] = 0
while q:
    x,y = q.popleft()
    if y == t:
        print(visit[(x,y)])
        break
    for dx in range(-2,3):
        for dy in range(-2,3):
            nx,ny = x+dx,y+dy
            if (nx,ny) not in visit and (nx,ny) in s:
                visit[(nx,ny)] = visit[(x,y)]+1
                q.append((nx,ny))
else:
    print(-1)