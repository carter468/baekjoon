# 가희의 고구마 먹방
# Gold 5, 브루트포스

import sys
input = sys.stdin.readline

def find_G():
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'G':
                return i,j
            
r,c,t = map(int,input().split())
grid = [input() for _ in range(r)]

nq = [(*find_G(),set())]
for _ in range(t):
    q = nq
    nq = []
    for x,y,count in q:
        for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if nx<0 or nx==r or ny<0 or ny==c or grid[nx][ny]=='#': continue
            nc = count.copy()
            if grid[nx][ny]=='S':
                nc.add((nx,ny))
            nq.append((nx,ny,nc))

result = 0
for a,b,count in nq:
    result = max(result,len(count))
print(result)