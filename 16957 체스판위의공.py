# 체스판 위의 공
# Gold 3, disjoint set

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(i,j,ni,nj):
    if (i,j) == (ni,nj): return
    a = find(i*c+j)
    b = find(ni*c+nj)
    root[a] = b
    ni,nj = divmod(b,c)
    count[ni][nj] += count[i][j]
    count[i][j] = 0

r,c = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(r)]

root = list(range(r*c))
count = [[1]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        m = (arr[i][j],i,j)
        for ni,nj in (i+1,j-1),(i+1,j),(i+1,j+1),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j),(i-1,j+1):
            if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] < m[0]:
                m = (arr[ni][nj],ni,nj)
        union(i,j,m[1],m[2])
        
for c in count:
    print(*c)