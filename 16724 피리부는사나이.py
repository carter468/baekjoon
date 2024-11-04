# 피리 부는 사나이
# Gold 3, disjoint set

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

D = {'D':(1,0),'U':(-1,0),'L':(0,-1),'R':(0,1)}

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

n,m = map(int,input().split())
arr = [input() for _ in range(n)]

root = list(range(n*m))
for x in range(n):
    for y in range(m):
        dx,dy = D[arr[x][y]]
        nx,ny = x+dx,y+dy
        a,b = find(x*m+y),find(nx*m+ny)
        root[a] = b

count = 0
for i in range(n):
    for j in range(m):
        a = i*m+j
        if find(a) == a: count += 1
print(count)