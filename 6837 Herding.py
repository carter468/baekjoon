# Herding
# Gold 3, disjoint set

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,M = map(int,input().split())
grid = [input() for _ in range(N)]

root = list(range(N*M))
for x in range(N):
    for y in range(M):
        dx,dy = {'N':(-1,0),'S':(1,0),'E':(0,1),'W':(0,-1)}[grid[x][y]]
        nx,ny = x+dx,y+dy
        root[find(x*M+y)] = find(nx*M+ny)

count = 0
for i in range(N*M):
    count += find(i) == i
print(count)