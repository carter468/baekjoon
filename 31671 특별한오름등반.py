# 특별한 오름 등반
# Gold 5, DFS

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = set([tuple(map(int,input().split())) for _ in range(m)])

visited = set()
q = [(0,0,0)]
while q:
    x,y,h = q.pop()
    if (x,y) == (n*2,0):
        print(h)
        break
    for nx,ny in (x+1,y-1),(x+1,y+1):
        if ny >= 0 and nx+ny <= n*2 and (nx,ny) not in arr and (nx,ny) not in visited:
            q.append((nx,ny,max(h,ny)))
            visited.add((nx,ny))
else: print(-1)